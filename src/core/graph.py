class DirectedGraph:
    """
    Representa um grafo dirigido usando lista de adjacência.

    No contexto do projeto Rastro Financeiro, o grafo é dirigido
    uma transação possui sentido: uma conta envia e outra conta recebe.

    Exemplo:
        Conta A -> Conta B

    Isso é diferente de:
        Conta B -> Cinta A
    """

    def __init__(self):
        # Dicionário principal da lista de adjacência
        # Cada chave é um vértice e cada valor é uma lista de vizinhos.
        self.adjacency_list = {}

        # Guarda informações extras das arestas, como tipo da relação e peso.
        self.edges_data = {}

    def add_vertex(self, vertex):
        """
        Adiciona um vértice ao grafo, caso ele ainda não exista.

        Complexidade: O(1), pois a consulta em dicionário é constante em média.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, origin, destination, weight=1, relation="transacao"):
        """
        Adiciona uma aresta dirigida ao grafo.

        Importante:
        Como o grafo é dirigido, adicionamos apenas origin -> destination.
        Não adicionamos destination -> origin automaticamente.

        Complexidade: O(1), considerando inserção simples em lista e dicionário.
        """
        self.add_vertex(origin)
        self.add_vertex(destination)

        self.adjacency_list[origin].append(destination)

        self.edges_data[(origin, destination)] = {
            "weight": weight,
            "relation": ralation 
        }
    
    def get_neighbors(self, vertex):
        """
        Retorna os vizinhos de saída de um vértice.

        Complexidade: O(1), pois acessa diretamente o dicionário.
        """
        return self.adjacency_list.get(vertex, [])
    
    def get_vertices(self):
        """
        Retorna todos os vértices cadastrados no grafo.

        Complexidade: O(V), pois retorna todos os vértices existentes.
        """
        return self.edges_data.get((origin, destination), {})
    
    def is_empty(self):
        """
        Verifica se o grafo está vazio.
        """
        return len(self.adjacency_list) == 0