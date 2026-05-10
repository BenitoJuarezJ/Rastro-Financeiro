from src.core.graph import DirectedGraph


def test_add_vertex():
    graph = DirectedGraph()
    graph.add_vertex("conta_001")

    assert "conta_001" in graph.get_vertices()


def test_add_directed_edge():
    graph = DirectedGraph()
    graph.add_edge("conta_001", "conta_002")

    assert "conta_002" in graph.get_neighbors("conta_001")

    # Como o grafo é dirigido, a volta não deve existir automaticamente.
    assert "conta_001" not in graph.get_neighbors("conta_002")


def test_empty_graph():
    graph = DirectedGraph()

    assert graph.is_empty() is True