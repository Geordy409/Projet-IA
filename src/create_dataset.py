import json

# Exemples de schémas et descriptions
schemas = [
    {
        "id": 1,
        "description": "Schéma représentant un diagramme de flux avec trois étapes : Entrée, Traitement, Sortie.",
        "schema_type": "diagramme de flux",
        "image_path": "data/images/flux_diagram.png"
    },
    {
        "id": 2,
        "description": "Organigramme d’une entreprise avec différents départements.",
        "schema_type": "organigramme",
        "image_path": "data/images/organisation_chart.png"
    },
]

# Sauvegarder les données dans un fichier JSON
with open("data/schemas.json", "w") as file:
    json.dump(schemas, file, indent=4)

print("Dataset créé et sauvegardé dans 'data/schemas.json'.")
