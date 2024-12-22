import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer
import openai

# Charger le dataset
try:
    with open("data/schemas.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Erreur : Le fichier 'data/schemas.json' est introuvable.")
    exit(1)
except json.JSONDecodeError:
    print("Erreur : Le fichier 'data/schemas.json' contient des erreurs de format JSON.")
    exit(1)

# Extraire les descriptions
try:
    descriptions = [item["description"] for item in data]
except KeyError:
    print("Erreur : Le format des données ne contient pas la clé 'description'.")
    exit(1)

# Charger le modèle pour générer des embeddings
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(descriptions)
except Exception as e:
    print(f"Erreur lors de la génération des embeddings : {e}")
    exit(1)

# Créer l'index FAISS
try:
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype('float32'))
except Exception as e:
    print(f"Erreur lors de la création de l'index FAISS : {e}")
    exit(1)

# Sauvegarder l'index
try:
    faiss.write_index(index, "data/faiss_index.bin")
    print(f"Index créé et sauvegardé avec {len(descriptions)} éléments.")
except Exception as e:
    print(f"Erreur lors de la sauvegarde de l'index FAISS : {e}")
    exit(1)

# Assigner directement la clé API OpenAI
openai.api_key = "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"

def generate_response_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # ou "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "Tu es un assistant qui explique les concepts de manière claire."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.OpenAIError as e:
        print(f"Erreur lors de la génération de la réponse GPT : {e}")
        return None

def enriched_search(query):
    try:
        # Étape 1 : Rechercher dans FAISS
        query_embedding = model.encode([query]).astype('float32')
        distances, indices = index.search(query_embedding, k=1)

        # Étape 2 : Récupérer la description correspondante
        best_match = descriptions[indices[0][0]]

        # Étape 3 : Générer une réponse détaillée avec GPT
        prompt = f"Explique en détail : {best_match}"
        response = generate_response_gpt(prompt)

        if response is None:
            print("Erreur : Impossible de générer une réponse avec GPT.")
            return None

        return {
            "query": query,
            "best_match": best_match,
            "generated_response": response
        }
    except Exception as e:
        print(f"Erreur lors de la recherche enrichie : {e}")
        return None


query = "Crée un diagramme qui explique le creative thinking"
result = enriched_search(query)
if result:
    print("Query :", result["query"])
    print("Best Match :", result["best_match"])
    print("Generated Response :", result["generated_response"])
