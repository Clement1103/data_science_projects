---------- ENGLISH VERSION BELOW ----------
## 💭 Présentation
Bonjour,

Je m'appelle Clément Baraille et je suis un étudiant nouvellement diplômé de l'école d'ingénieur Grenoble-INP Phelma. A travers mes stages, je me suis découvert un intérêt particulier pour la Data Science, particulièrement dans le domaine de la santé. 
C’est pour cette raison que j’approfondis les connaissances acquises lors de mon dernier stage au sein d’Orange, par une auto-formation rigoureuse sur les fondamentaux du Machine Learning et du Deep Learning. En complément de mon apprentissage, j'ai réalisé quelques projets, consignés dans ce dépôt que je tiens à jour très régulièrement. Les sujets sont variés et n'ont pas de lien entre eux, mais m'ont permis d'explorer différents types de données. Voici pour l'instant les projets réalisés :  
- Prédiction de loyers de maison à partir de données tabulaires : dataframes, nettoyage des données, outliers removal, GridSearchCV
- Classifications d'athlètes à l'aide de modèles de ML : traitement d'images, feature extraction à l'aide d'haar cascade, différentes transformations d'images, GridSearchCV
- Génération de mélodies avec des RNN : traitement de données musicales avec la librairie music21, génération d'un dataset à partir de séries temporelles, RNN, LSTM (Tensorflow) (consulter le README propre au projet)
- Détection d'anomalies dans un ECG : séries temporelles, LSTM auto-encoder (Pytorch)
- Segmentation automatique de matière grise dans les IRM de moelle épinière : images nifti, masques, U-net (Pytorch)
- Je suis actuellement en train de travailler sur un chatbot permettant de répondre à certaines questions d'un collaborateur à propos de divers produits de santé dans une entreprise fictive.

Ce sont pour l'instant les premiers projets que j'ai réalisés. J'ai l'intention d’en rajouter rapidement de nouveaux, notamment en NLP, domaine sur lequel je me forme actuellement.

## 📝 Installation 

Dans le cas où vous voudriez ouvrir mes projets sur votre machine, j'ai créé des fichiers requirements.txt, ainsi que des fichiers .yml permettant de reproduire l'environnement conda (un pour les deux projets de ML, et un par projet de DL).

Pour reproduire mon environnement conda si conda est déjà installé sur votre machine :
```
conda env create -f <fichier.yml>
conda env list # pour trouver le nom de l'environnement
conda activate <nom_de_l'environnement>
```
Ou bien pour installer dans un environnement existant à l'aide de pip : 
```
pip install -r requirements.txt
```
Ensuite, les notebooks peuvent être consultés à l'aide de :
```
jupyter notebook
```

**Néanmoins, pour éviter d'avoir à installer cela, j'ai téléchargé les notebooks en pdf, qui sont consultables sans environnement.**


## 💡 Mot de la fin

J'espère que ces projets vous intéresseront autant qu'ils m'ont intéressé, et que j'aurai l'occasion de vous démontrer mes compétences.
Enfin, je suis toujours ouvert à une quelconque suggestion de projet, ou encore aux remarques concernant ce dépôt.

Bonne journée !

===========================

## 💭 Presentation
Hello,

My name is Clément Baraille and I'm a recent graduate of Grenoble-INP Phelma engineering school. Through my internships, I have discovered a particular interest in Data Science, particularly in the healthcare field. 
That's why I'm deepening the knowledge I acquired during my last internship with Orange, through rigorous self-training on the fundamentals of Machine Learning and Deep Learning. In addition to my apprenticeship, I have carried out a number of projects, which are recorded in this repository that I update regularly. The subjects are varied and unrelated, but have enabled me to explore different types of data. 
For now, here are the projects I've completed:  
- House rent prediction from tabular data: dataframes, data cleaning, outlier removal, GridSearchCV
- Athlete classifications using ML models: image processing, feature extraction using haar cascade, various image transformations, GridSearchCV
- Melody generation with RNN: music data processing with the music21 library, dataset generation from time series, RNN, LSTM (Tensorflow) (see project-specific README)
- ECG anomaly detection: time series, LSTM auto-encoder (Pytorch)
- Gray-matter segmentation project in spinal cord MRIs : nifti files, masks, U-net (Pytorch)
- Currently working on a chatbot which aims to answer questions about health products from a fictive company.

So far, these are the first projects I've completed. 
I intend to quickly add new projects, particularly in NLP, a field in which I'm currently training. 

## 📝 Installation 

In case you'd like to open my projects on your machine, I've created requirements.txt files, as well as .yml files to reproduce the conda environment (one for the two ML projects, and one for each DL project).

To reproduce my conda environment if conda is already installed on your machine:
```
conda env create -f <fichier.yml>
conda env list # to find the environment name
conda activate <environment_name>
```
Or to install in an existing environment using pip : 
```
pip install -r requirements.txt
```
Notebooks can then be viewed using :
```
jupyter notebook
```

**However, to avoid having to install this, I've downloaded the notebooks as pdf files, which can be viewed without an environment.**

## 💡 Closing remarks

So far, these are the first projects I've completed. I intend to add new ones soon, especially in NLP, a field I'm currently training in.

Have a nice day!
