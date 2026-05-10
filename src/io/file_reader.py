import json
from src.core.graph import DirectedGraph


def read_graph_from_json(file_path):
    """
    Lê um arquivo JSON e cria um grafo dirigido a partir dele.

    O arquivo deve conter uma lista de arestas com origem, destino,
    tipo de relação e peso.

    Complexidade: O(V + E), pois percorre as arestas e cria os vértices.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    graph = DirectedGraph()

    for edge in data.get("arestas", []):
        origin = edge["origem"]
        destination = edge["destino"]
        weight = edge.get("peso", 1)
        relation = edge.get("relacao", "transacao")

        graph.add_edge(origin, destination, weight, relation)

    return graph