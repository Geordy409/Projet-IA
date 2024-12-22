from flask import Flask, render_template, request
from src.enriched_search import enriched_search
import graphviz
import os
from shutil import copyfile

app = Flask(__name__)

# Chemins des fichiers
STATIC_IMAGES_PATH = "static/images"
DATA_IMAGES_PATH = "data/images"

# Assurez-vous que les répertoires existent
os.makedirs(STATIC_IMAGES_PATH, exist_ok=True)
os.makedirs(DATA_IMAGES_PATH, exist_ok=True)

def generate_schema(schema_data, output_file):
    """
    Génère un diagramme avec Graphviz.
    Args:
        schema_data (dict): Données du schéma (nœuds, relations).
        output_file (str): Chemin pour sauvegarder l'image générée.
    """
    dot = graphviz.Digraph()

    # Ajouter les nœuds
    for node in schema_data["nodes"]:
        dot.node(node["id"], node["label"])

    # Ajouter les relations
    for edge in schema_data["edges"]:
        dot.edge(edge["source"], edge["target"], label=edge.get("label", ""))

    # Sauvegarder l'image
    dot.render(output_file, format="png", cleanup=True)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_query = request.form.get("query")
        if user_query:
            # Étape 1 : Recherche enrichie
            result = enriched_search(user_query)
            if result is None:
                return render_template("index.html", error="Erreur lors de la recherche enrichie.")

            # Étape 2 : Convertir le résultat en données JSON pour le schéma
            schema_data = {
                "nodes": [
                    {"id": "1", "label": "Start"},
                    {"id": "2", "label": "Process"},
                    {"id": "3", "label": "End"},
                ],
                "edges": [
                    {"source": "1", "target": "2", "label": "Step 1"},
                    {"source": "2", "target": "3", "label": "Step 2"},
                ],
            }

            # Étape 3 : Générer le diagramme
            output_file = os.path.join(DATA_IMAGES_PATH, "generated_schema")
            generate_schema(schema_data, output_file)

            # Copier l'image dans le dossier static pour affichage
            static_file = os.path.join(STATIC_IMAGES_PATH, "generated_schema.png")
            copyfile(f"{output_file}.png", static_file)

            # Rendre le template avec l'image générée
            return render_template(
                "index.html",
                image_url=f"/{static_file}",
                query=result["query"],
                response=result["generated_response"],
            )

    return render_template("index.html", image_url=None)


if __name__ == "__main__":
    app.run(debug=True)
