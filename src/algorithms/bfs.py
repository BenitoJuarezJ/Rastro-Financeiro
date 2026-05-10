from collections import deque


def bfs(graph, start_vertex):
    """
    Executa Busca em Largura, BFS, em um grafo dirigido.

    A BFS percorre o grafo em camadas. No projeto Rastro Financeiro,
    ela ajuda a descobrir contas, CPFs ou IPs conectados a partir de
    uma entidade inicial suspeita.

    Complexidade de tempo: O(V + E)
    Complexidade de espaço: O(V)
    """
    if graph.is_empty():
        return []

    if start_vertex not in graph.get_vertices():
        return []

    visited = set()
    queue = deque([start_vertex])
    result = []

    while queue:
        current_vertex = queue.popleft()

        if current_vertex in visited:
            continue

        visited.add(current_vertex)
        result.append(current_vertex)

        for neighbor in graph.get_neighbors(current_vertex):
            if neighbor not in visited:
                queue.append(neighbor)

    return result
