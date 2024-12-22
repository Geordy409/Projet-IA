# Projet-IA

#  Projet : Concevoir un système capable de reproduire les schémas de manière interactive

## Description

Ce projet RAG vise à concevoir un système interactif capable de générer des schémas visuels à partir de descriptions textuelles. En combinant les techniques de recherche vectorielle avec l'indexation (FAISS) et les modèles de langage naturel (NLP), le système permet de :

- Rechercher des informations pertinentes à partir d'une base de données.
- Transformer ces informations en schémas structurés et visuels.
- Offrir une interface utilisateur pour des interactions fluides.

## Fonctionnalités principales

1. **Recherche enrichie** : Recherche vectorielle rapide grâce à FAISS, couplée à un modèle NLP pour générer des réponses détaillées.
2. **Génération de schémas** : Création automatique de schémas à partir de descriptions enrichies.
3. **Interface utilisateur** : Application web interactive permettant aux utilisateurs de soumettre des descriptions et d'obtenir des schémas visuels.

## Technologies utilisées

- **Indexation** : FAISS
- **Modèles NLP** : GPT-3, T5, ou BERT
- **Pipeline RAG** : LangChain
- **Visualisation graphique** : Graphviz, Matplotlib, NetworkX
- **Interface utilisateur** : Flask

## Prérequis

- Python 3.8+
- Outils installés :
  - FAISS
  - Sentence Transformers
  - Flask
  - Matplotlib
  - NetworkX

## Installation

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/Geordy409/Projet-IA.git
   
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Structure du projet

```plaintext
RAG-Schema-Generator/
├── app.py                   # Application Flask principale
├── data/
│   ├── schemas.json         # Dataset annoté des schémas
│   ├── faiss_index.bin      # Index FAISS généré
│   ├── images/              # Schémas ou exemples associés
├── src/
│   ├── create_dataset.py    # Script pour collecter/structurer les données
│   ├── faiss_index.py       # Script pour créer l'index FAISS
│   ├── enriched_search.py   # Recherche enrichie avec NLP
├── templates/
│   └── index.html           # Interface utilisateur HTML
├── notebooks/
│   ├── exploration.ipynb    # Notebook pour tester les données
├── requirements.txt         # Dépendances Python
└── README.md                # Documentation du projet
```

## Utilisation

1. **Lancer l'application Flask** :
   ```bash
   python app.py
   ```

2. Accédez à l'interface utilisateur via [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. **Entrer une description** : Fournissez une description textuelle (ex. : "Créer un organigramme pour une entreprise avec trois départements").

4. **Visualiser le schéma généré** : Le système affiche le schéma correspondant.

## Développement

### Étapes principales

1. **Préparation des données** :
   - Collecte de schémas annotés (JSON ou CSV).
   - Génération d'embeddings avec Sentence Transformers.

2. **Création de l'index FAISS** :
   - Stockage des embeddings pour des recherches rapides.

3. **Intégration NLP et RAG** :
   - Enrichissement des recherches via un modèle NLP.
   - Génération de structures JSON ou GraphML.

4. **Affichage des schémas** :
   - Génération graphique avec Matplotlib ou NetworkX.
   - Interface utilisateur avec Flask.

## Contributions

Les contributions sont les bienvenues !

1. Forkez le dépôt.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b feature/ajout-fonctionnalité
   ```
3. Effectuez un pull request une fois vos modifications terminées.

