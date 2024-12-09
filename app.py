from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import networkx as nx
import os

app = Flask(__name__)

def generate_schema_with_matplotlib(schema_data, output_file="output_schema"):
    G = nx.DiGraph()

    for node in schema_data['nodes']:
        G.add_node(node['id'], label=node['label'])

    for edge in schema_data['edges']:
        G.add_edge(edge['source'], edge['target'], label=edge.get('label', ''))

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')

    plt.title("Schéma Généré")
    plt.savefig(output_file)
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_query = request.form.get('query')
        # Vous pouvez ici intégrer la fonction `enriched_search` pour enrichir la requête
        schema_data = {
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

        output_file = "images/organigramme.png"
        generate_schema_with_matplotlib(schema_data, output_file)

        return render_template('index.html', image_url=output_file)
    return render_template('index.html', image_url=None)

if __name__ == '__main__':
    app.run(debug=True)
