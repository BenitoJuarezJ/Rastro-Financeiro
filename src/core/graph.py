class DirectedGraph:
    """
    Grafo dirigido implementado com lista de adjacência.

    No projeto Rastro Financeiro:
    - vértices representam contas, CPFs, IPs ou outras entidades;
    - arestas representam relações dirigidas, como transações e acessos.
    """

    def __init__(self):
        """
        Inicializa as estruturas internas do grafo.

        Complexidade de tempo: O(1)
        Complexidade de espaço: O(1)
        """
        self.adjacency_list = {}
        self.edges_data = {}

    def add_vertex(self, vertex):
        """
        Adiciona um vértice ao grafo, caso ele ainda não exista.

        Complexidade de tempo: O(1)
        Complexidade de espaço: O(1)
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, origin, destination, relation="transacao", weight=1, value=None):
        """
        Adiciona uma aresta dirigida ao grafo.

        Como o grafo é dirigido, adicionamos apenas origin -> destination.
        A aresta destination -> origin não é criada automaticamente.

        Complexidade de tempo: O(1)
        Complexidade de espaço: O(1)
        """
        self.add_vertex(origin)
        self.add_vertex(destination)

        # Evita repetir o mesmo destino na lista de adjacência.
        if destination not in self.adjacency_list[origin]:
            self.adjacency_list[origin].append(destination)

        self.edges_data[(origin, destination)] = {
            "relation": relation,
            "weight": weight,
            "value": value,
        }

    def get_vertices(self):
        """
        Retorna todos os vértices do grafo.

        Complexidade de tempo: O(V)
        """
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        """
        Retorna os vizinhos de saída de um vértice.

        Complexidade de tempo: O(1), em média, por acesso em dicionário.
        """
        return self.adjacency_list.get(vertex, [])

    def get_edge_data(self, origin, destination):
        """
        Retorna os dados de uma aresta específica.

        Complexidade de tempo: O(1)
        """
        return self.edges_data.get((origin, destination), {})

    def get_edges(self):
        """
        Retorna todas as arestas com seus metadados.

        Complexidade de tempo: O(E)
        """
        edges = []

        for edge_key, edge_data in self.edges_data.items():
            origin, destination = edge_key
            edges.append((origin, destination, edge_data))

        return edges

    def is_empty(self):
        """
        Verifica se o grafo está vazio.

        Complexidade de tempo: O(1)
        """
        return len(self.adjacency_list) == 0

    def number_of_vertices(self):
        """
        Retorna a quantidade de vértices.

        Complexidade de tempo: O(1)
        """
        return len(self.adjacency_list)

    def number_of_edges(self):
        """
        Retorna a quantidade de arestas.

        Complexidade de tempo: O(1)
        """
        return len(self.edges_data)
