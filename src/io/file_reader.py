import json
from pathlib import Path

from src.core.graph import DirectedGraph


class GraphFileError(Exception):
    """Erro específico para falhas na leitura do arquivo JSON do grafo."""


def _validate_text_field(edge, field_name, edge_index):
    """Valida campos obrigatórios de texto dentro de uma aresta."""
    if field_name not in edge:
        raise GraphFileError(
            "A aresta na posição {} não possui o campo obrigatório '{}'.".format(
                edge_index,
                field_name,
            )
        )

    value = edge[field_name]

    if not isinstance(value, str) or not value.strip():
        raise GraphFileError(
            "O campo '{}' da aresta na posição {} deve ser um texto não vazio.".format(
                field_name,
                edge_index,
            )
        )

    return value.strip()


def read_graph_from_json(file_path):
    """
    Lê um arquivo JSON e cria um grafo dirigido.

    Formato esperado:
    {
      "vertices": ["conta_001", "conta_002"],
      "arestas": [
        {
          "origem": "conta_001",
          "destino": "conta_002",
          "relacao": "transacao",
          "peso": 1,
          "valor": 500.0
        }
      ]
    }

    Complexidade de tempo: O(V + E)
    Complexidade de espaço: O(V + E)
    """
    path = Path(file_path)

    if not path.exists():
        raise GraphFileError("Arquivo não encontrado: {}".format(file_path))

    if not path.is_file():
        raise GraphFileError("O caminho informado não é um arquivo: {}".format(file_path))

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        raise GraphFileError(
            "O arquivo '{}' não contém um JSON válido. Detalhe: {}".format(
                file_path,
                error,
            )
        )

    if not isinstance(data, dict):
        raise GraphFileError("O conteúdo principal do JSON precisa ser um objeto.")

    graph = DirectedGraph()

    vertices = data.get("vertices", [])
    if vertices:
        if not isinstance(vertices, list):
            raise GraphFileError("O campo 'vertices' precisa ser uma lista.")

        for vertex in vertices:
            if not isinstance(vertex, str) or not vertex.strip():
                raise GraphFileError("Todos os vértices precisam ser textos não vazios.")

            graph.add_vertex(vertex.strip())

    edges = data.get("arestas")
    if edges is None:
        raise GraphFileError("O JSON precisa possuir o campo obrigatório 'arestas'.")

    if not isinstance(edges, list):
        raise GraphFileError("O campo 'arestas' precisa ser uma lista.")

    for index, edge in enumerate(edges, start=1):
        if not isinstance(edge, dict):
            raise GraphFileError("A aresta na posição {} precisa ser um objeto.".format(index))

        origin = _validate_text_field(edge, "origem", index)
        destination = _validate_text_field(edge, "destino", index)
        relation = str(edge.get("relacao", "transacao")).strip() or "transacao"
        weight = edge.get("peso", 1)
        value = edge.get("valor", None)

        graph.add_edge(
            origin=origin,
            destination=destination,
            relation=relation,
            weight=weight,
            value=value,
        )

    return graph
