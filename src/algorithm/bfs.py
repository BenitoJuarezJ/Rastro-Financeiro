from collections import deque


def bfs(graph, start_vertex):
    """
    Executa Busca em Largura (BFS) em um grafo dirigido.

    No projeto, a BFS ajuda a descobrir quais contas, CPFs ou IPs estão
    conectados a partir de um ponto inicial suspeito.

    Complexidade de tempo: O(V + E)
        V = número de vértices
        E = número de arestas

    Complexidade de espaço: O(V)
        Por causa da fila e do conjunto de visitados.
    """

    if graph.is_empty():
        return []

    if start_vertex not in graph.adjacency_list:
        return []

    visited = set()
    queue = deque([start_vertex])
    result = []

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            result.append(current)

            for neighbor in graph.get_neighbors(current):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result