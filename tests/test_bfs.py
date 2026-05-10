from src.core.graph import DirectedGraph
from src.algorithms.bfs import bfs


def test_bfs_base_case():
    graph = DirectedGraph()
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")

    result = bfs(graph, "A")

    assert result == ["A", "B", "C"]


def test_bfs_empty_graph():
    graph = DirectedGraph()

    result = bfs(graph, "A")

    assert result == []


def test_bfs_complete_graph():
    graph = DirectedGraph()
    vertices = ["A", "B", "C"]

    for origin in vertices:
        for destination in vertices:
            if origin != destination:
                graph.add_edge(origin, destination)

    result = bfs(graph, "A")

    assert set(result) == {"A", "B", "C"}