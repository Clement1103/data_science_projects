import torch
import numpy as np
from torch.utils.data import DataLoader, Dataset
from transformers import DistilBertTokenizer, DistilBertModel
from tqdm import tqdm
import argparse
import os
import pandas as pd

from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

s3_uri = os.getenv("S3_URI")

df = pd.read_csv(s3_uri, sep='\t', names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])
df_work = df[['TITLE', 'CATEGORY']]
my_dict = {
    'b':'Business',
    'e':'Entertainment',
    't':'Technology',
    'm':'Medicine'
}

df_work['CATEGORY'] = df_work['CATEGORY'].apply(lambda x: my_dict[x])

print('[INFO] Pre-processing done.')

# Ici, je sous-échantillonne le jeu pour réduire le temps d'entraînement, et donc les coûts engendrés. Le modèle issu de cet entraînement sera donc mauvais, fera probablement de l'overfitting. Je veux ici m'assurer que j'arrive à lancer correctement l'entraînement, et j'utiliserai un modèle entraîné sur le jeu complet pour la suite. 
df = df_work.sample(frac=0.05, random_state=11)
df = df.reset_index(drop=True)

print('Resulting dataframe :\n', df)

categories = list(df['CATEGORY'].unique())
df['CATEGORY'] = df['CATEGORY'].apply(lambda x: categories.index(x) if x in categories else len(categories))

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')


class NewsDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_len):
        self.len = len(dataframe)
        self.data = dataframe
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __getitem__(self, index):
        title = str(self.data.TITLE.iloc[index])
        # title = str(self.data.TITLE[index])
        title = ' '.join(title.split())

        inputs = self.tokenizer.encode_plus(
            title,
            None,
            add_special_tokens = True,
            max_length = self.max_len,
            padding = 'max_length',
            truncation = True,
            return_token_type_ids = True,
            return_attention_mask = True
        )

        output = {
            'ids': torch.tensor(inputs['input_ids'], dtype=torch.long),
            'mask': torch.tensor(inputs['attention_mask'], dtype=torch.long),
#            'targets': torch.tensor(self.data.CATEGORY.[index], dtype=torch.long)
            'targets': torch.tensor(self.data.CATEGORY.iloc[index], dtype=torch.long)
        }
        return output

    def __len__(self):
        return self.len


train_size = 0.8
train_dataset = df.sample(frac=train_size, random_state=11)
test_dataset = df.drop(train_dataset.index).reset_index(drop=True)

train_dataset.reset_index(drop=True)

print(f'Full dataset shape: {df.shape}')
print(f'Train dataset shape: {train_dataset.shape}')
print(f'Test dataset shape: {test_dataset.shape}')

MAX_LEN = 512
TRAIN_BATCH_SIZE = 4
VALID_BATCH_SIZE = 2

training_set = NewsDataset(train_dataset, tokenizer, MAX_LEN)
testing_set = NewsDataset(test_dataset, tokenizer, MAX_LEN)

train_parameters = {
    'batch_size':TRAIN_BATCH_SIZE,
    'shuffle': True,
    'num_workers': 0
}

test_parameters = {
    'batch_size':VALID_BATCH_SIZE,
    'shuffle': True,
    'num_workers': 0
}

training_loader = DataLoader(training_set, **train_parameters)
testing_loader = DataLoader(testing_set, **test_parameters)

# * Mon modèle prend en entrée un texte,
# * La première couche calcule les embeddings,
# * Je sélectionne l'embedding du token [CLS] qui contient des informations concernant l'ensemble de la phrase,
# * J'effectue la classification sur ce vecteur d'embedding après l'avoir passé dans une couche ReLu puis une couche de dropout 

class DistilBERTClass(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = DistilBertModel.from_pretrained('distilbert-base-uncased')
        self.pre_classifier = torch.nn.Linear(768, 768)
        self.dropout = torch.nn.Dropout(0.3)
        self.classifier = torch.nn.Linear(768, 4)

    def forward(self, input_ids, attention_mask):
        output_1 = self.l1(input_ids=input_ids, attention_mask=attention_mask)
        hidden_state = output_1[0]
        pooler = hidden_state[:,0]
        pooler = self.pre_classifier(pooler)
        pooler = torch.nn.ReLU()(pooler)
        pooler = self.dropout(pooler)
        output = self.classifier(pooler)
        return output

def calculate_acc(predictions, targets):
    n_correct = (predictions == targets).sum().item()
    return n_correct
    
def train_model(model, training_loader, epoch, device, loss_function, optimizer):
    tr_loss = 0
    n_correct = 0
    nb_tr_step = 0
    nb_tr_examples = 0
    model.train()

    for k, data in enumerate(training_loader, 0):
        ids = data['ids'].to(device, dtype = torch.long)
        mask = data['mask'].to(device, dtype = torch.long)
        targets = data['targets'].to(device, dtype = torch.long)

        pred = model(ids, mask)

        loss = loss_function(pred, targets)
        tr_loss += loss.item() # Ex : Permet de passer de tensor(4) à 4

        pred_val, pred_idx = torch.max(pred.data, dim=1)
        n_correct += calculate_acc(pred_idx, targets)

        nb_tr_step += 1
        nb_tr_examples += targets.size(0)

        if k % 5000 == 0: # Attention à ne pas confondre le nb steps et le nb d'epochs (par exemple, si on a 100 000 échantillons dans le jeu d'entraînement, il y aura 25 000 steps (puisque batch_size = 4))
            loss_step = tr_loss / nb_tr_step
            accu_step = (n_correct*100)/nb_tr_examples
            print(f'Training loss per 5000 steps: {loss_step}')
            print(f'Training accuracy per 5000 steps: {accu_step}')

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    epoch_loss = tr_loss / nb_tr_step
    epoch_acc = (n_correct*100)/nb_tr_examples
    print(f'Total training accuracy for epoch {epoch}: {epoch_acc}')
    print(f'Training loss for epoch {epoch}: {epoch_loss}')

    return 
    
def eval_model(model, testing_loader, epoch, device, loss_function):
    val_loss = 0
    n_correct = 0
    nb_v_step = 0
    nb_v_examples = 0
    model.eval()
    with torch.no_grad():
        for k, data in enumerate(testing_loader):
            ids = data['ids'].to(device, dtype = torch.long)
            mask = data['mask'].to(device, dtype = torch.long)
            targets = data['targets'].to(device, dtype = torch.long)

            pred = model(ids, mask)

            loss = loss_function(pred, targets)
            val_loss += loss.item()

            pred_val, pred_idx = torch.max(pred.data, dim=1)
            n_correct = calculate_acc(pred_idx, targets)

            nb_v_step += 1
            nb_v_examples += targets.size(0)
    
            if k % 1000 == 0:
                loss_step = val_loss / nb_v_step
                accu_step = (n_correct*100)/nb_v_examples
                print(f'Validation loss per 1000 steps: {loss_step}')
                print(f'Validation accuracy per 1000 steps: {accu_step}')

    epoch_loss = val_loss / nb_v_step
    epoch_acc = (n_correct*100)/nb_v_examples
    print(f'Total validation accuracy for epoch {epoch}: {epoch_acc}')
    print(f'Validation loss for epoch {epoch}: {epoch_loss}')
    return


def main():
    print('Start')
    # On peut définir les hyperparamètres manuellement, mais ce n'est pas ce qu'on fera ici
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--epochs', type=int, default=10)
    # args = parser.parse_args()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBERTClass()
    model.to(device)

    LEARNING_RATE = 1e-05
    optimizer = torch.optim.Adam(params=model.parameters(), lr=LEARNING_RATE)
    loss_function = torch.nn.CrossEntropyLoss()

    EPOCHS = 4
    for epoch in range(EPOCHS):
        print(f'Starting epoch: {epoch +1}')
        train_model(model, training_loader, epoch, device, loss_function, optimizer)
        eval_model(model, testing_loader, epoch, device, loss_function)

    output_dir = os.environ['SM_MODEL_DIR']
    output_model_file = os.path.join(output_dir, 'pytorch_distilbert_news_classif.bin')
    output_vocab_file = os.path.join(output_dir, 'vocab_distilbert_news_classif.bin')
    torch.save(model.state_dict(), output_model_file)
    tokenizer.save_vocabulary(output_vocab_file)

if __name__ == '__main__':
    main()