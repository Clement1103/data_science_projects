# Clément Baraille — Data Science Projects

## 💭 Présentation

Ingénieur diplômé de Grenoble-INP Phelma, je travaille comme Data Scientist avec une spécialisation en modèles de langage (LLM). Après une première expérience professionnelle chez Orange (classification, clustering, deep learning), je suis actuellement Data Scientist chez NVEIL à Grenoble, où je conçois et développe le micro-service IA d'un logiciel de visualisation analytique pilotée par chatbot — incluant l'orchestration d'un pipeline LLM + ASP via LangGraph, une abstraction multi-fournisseurs et une gestion de l'observabilité d'inférence en production.

Je suis à la recherche active de nouvelles opportunités pour continuer à progresser sur des problématiques IA exigeantes, dans un environnement collaboratif et stimulant.

---

## ⚠️ Note sur ce dépôt

Les projets présentés ici ont été réalisés **en 2023-2024**, dans le cadre de mon auto-formation en Data Science, peu après ma sortie d'école. Ils ont avant tout une vocation exploratoire et pédagogique.

Je suis tout à fait conscient qu'ils ne reflètent pas les standards attendus en milieu professionnel : pas de tests unitaires, peu de modularité, gestion des dépendances perfectible, et absence de considérations MLOps (monitoring, reproductibilité, versioning des modèles…).

Ces points constituent précisément ce que j'ai appris à adresser lors de mon expérience chez NVEIL — conception orientée production, observabilité par tour, gestion des coûts d'inférence, timeouts et budgets de retry. Mes réalisations professionnelles récentes ne sont pas publiques, mais je suis toujours disponible pour en discuter.

---

## 📂 Projets réalisés

Les sujets sont variés et m'ont permis d'explorer différents types de données et paradigmes de modélisation :

- **Prédiction de loyers** à partir de données tabulaires — nettoyage, outliers, GridSearchCV
- **Classification d'athlètes** — traitement d'images, extraction de features (Haar cascade), GridSearchCV
- **Génération de mélodies avec des RNN** — données musicales (music21), séries temporelles, LSTM (TensorFlow)
- **Détection d'anomalies dans un ECG** — séries temporelles, LSTM auto-encoder (PyTorch)
- **Segmentation de matière grise dans des IRM de moelle épinière** — fichiers NIfTI, masques, U-Net (PyTorch)
- **Chatbot de réponse aux questions collaborateurs** — NLP, Dialogflow, SQL, frontend
- **Fine-tuning de BERT pour la classification de titres d'articles** — SageMaker, HuggingFace, PyTorch

Un nouveau projet est actuellement en cours de finalisation et sera ajouté prochainement.

---

## 📝 Installation

Des fichiers `requirements.txt` et `.yml` sont disponibles pour reproduire les environnements conda.

```bash
# Reproduire l'environnement conda
conda env create -f <fichier.yml>
conda activate <nom_de_l_environnement>

# Ou via pip dans un environnement existant
pip install -r requirements.txt

# Lancer les notebooks
jupyter notebook
```

> Pour éviter toute installation, les notebooks sont également disponibles en PDF directement consultables.  
> Les jeux de données sont dans des dossiers `.zip` à décompresser avant exécution.

---

## 💡 Mot de la fin

Bonne lecture — et n'hésitez pas à me contacter si vous souhaitez échanger sur mes travaux plus récents ou discuter d'une opportunité.

---

*English version below.*

---

# Clément Baraille — Data Science Projects

## 💭 Presentation

I'm a graduate engineer from Grenoble-INP Phelma, working as a Data Scientist with a specialization in large language models (LLMs). After an internship at Orange (classification, clustering, deep learning), I'm currently a Data Scientist at NVEIL in Grenoble, where I design and develop the AI microservice of an analytics visualization software driven by a chatbot — including LLM + ASP pipeline orchestration via LangGraph, multi-provider abstraction, and production inference observability.

I'm actively looking for new opportunities to keep growing on challenging AI problems, in a collaborative and stimulating environment.

---

## ⚠️ Note on this repository

The projects here were built in **2023–2024** as part of my self-directed Data Science training, shortly after graduating. They are exploratory and educational in nature.

I'm fully aware they don't reflect professional production standards: no unit tests, limited modularity, improvable dependency management, and no MLOps considerations (monitoring, reproducibility, model versioning…).

These are precisely the areas I've grown in during my time at NVEIL — production-oriented design, per-turn observability, inference cost tracking, timeouts and retry budgets. My more recent professional work isn't public, but I'm always happy to discuss it.

---

## 📂 Projects

- **House rent prediction** from tabular data — cleaning, outlier removal, GridSearchCV
- **Athlete classification** — image processing, Haar cascade feature extraction, GridSearchCV
- **Melody generation with RNNs** — music data (music21), time series, LSTM (TensorFlow)
- **ECG anomaly detection** — time series, LSTM auto-encoder (PyTorch)
- **Gray matter segmentation in spinal cord MRIs** — NIfTI files, masks, U-Net (PyTorch)
- **Employee Q&A chatbot** — NLP, Dialogflow, SQL, frontend
- **BERT fine-tuning for article title classification** — SageMaker, HuggingFace, PyTorch

A new project is currently being finalized and will be added soon.

---

## 📝 Installation

```bash
conda env create -f <file.yml>
conda activate <environment_name>

# or via pip
pip install -r requirements.txt

jupyter notebook
```

> Notebooks are also available as PDFs — no installation needed.  
> Datasets are in `.zip` folders and need to be extracted before running notebooks.

---

## 💡 Closing remarks

Feel free to reach out if you'd like to discuss my more recent work or explore an opportunity together.
