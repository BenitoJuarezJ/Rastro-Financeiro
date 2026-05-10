from src.io.file_reader import read_graph_from_json


def test_read_graph_from_json_example_file():
    graph = read_graph_from_json("data/grafo_exemplo.json")

    assert graph.number_of_vertices() == 8
    assert graph.number_of_edges() == 9
    assert "conta_002" in graph.get_neighbors("conta_001")
    assert graph.get_edge_data("conta_001", "conta_002")["relation"] == "transacao"
