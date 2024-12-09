import matplotlib.pyplot as plt
import networkx as nx

def generate_schema_with_matplotlib(schema_data, output_file="output_schema"):
    """
    Génère un schéma visuel avec NetworkX et Matplotlib.
    Args:
        schema_data (dict): Les données du schéma (nœuds, relations).
        output_file (str): Nom du fichier de sortie (sans extension).
    """
    # Créer un graphe dirigé
    G = nx.DiGraph()

    # Ajouter les nœuds
    for node in schema_data['nodes']:
        G.add_node(node['id'], label=node['label'])

    # Ajouter les arêtes (relations)
    for edge in schema_data['edges']:
        G.add_edge(edge['source'], edge['target'], label=edge.get('label', ''))

    # Dessiner le graphique
    pos = nx.spring_layout(G)  # Choisir un layout pour disposer les nœuds
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')

    # Sauvegarder l'image du schéma
    plt.title("Schéma Généré")
    plt.savefig(f"{output_file}.png")
    plt.close()
    print(f"Schéma généré : {output_file}.png")


# Exemple de structure de données
example_schema = {
    "nodes": [
        {"id": "1", "label": "Direction Générale"},
        {"id": "2", "label": "Département RH"},
        {"id": "3", "label": "Département Marketing"},
    ],
    "edges": [
        {"source": "1", "target": "2", "label": "Supervision"},
        {"source": "1", "target": "3", "label": "Supervision"},
    ],
}

generate_schema_with_matplotlib(example_schema, output_file="data/images/organigramme")
