class DirectedGraph:
    def __init__(self):
        """
        Inicializa o grafo dirigido.

        adjacency_list: armazena os vértices e seus vizinhos.
        edges_data: armazena informações das arestas.

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

    def add_edge(self, origin, destination, relation="TRANSFERE", weight=1, value=None):
        """
        Adiciona uma aresta dirigida ao grafo.

        Atenção:
        Como o grafo é dirigido, adicionamos apenas origin -> destination.
        A aresta inversa não é criada automaticamente.

        Complexidade de tempo: O(1)
        Complexidade de espaço: O(1)
        """

        # Garante que os dois vértices existam no grafo
        self.add_vertex(origin)
        self.add_vertex(destination)

        # Adiciona a ligação dirigida: origem -> destino
        self.adjacency_list[origin].append(destination)

        # Armazena os dados da aresta
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

        Complexidade de tempo: O(1), acesso médio em dicionário.
        """
        return self.adjacency_list.get(vertex, [])

    def get_edge_data(self, origin, destination):
        """
        Retorna os dados de uma aresta específica.

        Complexidade de tempo: O(1)
        """
        return self.edges_data.get((origin, destination), {})

    def is_empty(self):
        """
        Verifica se o grafo não possui vértices.

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