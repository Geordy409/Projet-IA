import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

# Charger le dataset
with open("data/schemas.json", "r") as file:
    data = json.load(file)

# Extraire les descriptions
descriptions = [item["description"] for item in data]

# Charger le modèle pour générer des embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(descriptions)

# Créer l'index FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype('float32'))

# Sauvegarder l'index
faiss.write_index(index, "data/faiss_index.bin")

print(f"Index créé et sauvegardé avec {len(descriptions)} éléments.")

