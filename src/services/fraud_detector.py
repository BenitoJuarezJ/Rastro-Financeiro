def format_currency_br(value):
    """Formata número no padrão monetário brasileiro."""
    formatted = "{:,.2f}".format(value)
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


class FraudDetector:
    """
    Detecta padrões suspeitos em um grafo financeiro.

    Este MVP não afirma que houve fraude. Ele apenas gera alertas técnicos
    para apoiar uma investigação humana.
    """

    def __init__(self, graph):
        self.graph = graph

    def detect_high_out_degree_accounts(self, threshold=3):
        """
        Detecta vértices com muitas conexões de saída.

        Complexidade de tempo: O(V)
        Complexidade de espaço: O(A), onde A é a quantidade de alertas.
        """
        alerts = []

        for vertex in self.graph.get_vertices():
            neighbors = self.graph.get_neighbors(vertex)

            if len(neighbors) >= threshold:
                alerts.append(
                    {
                        "tipo": "alto_grau_saida",
                        "vertice": vertex,
                        "quantidade_conexoes": len(neighbors),
                        "mensagem": "{} possui muitas conexões de saída.".format(vertex),
                    }
                )

        return alerts

    def detect_shared_ip_patterns(self, threshold=3):
        """
        Detecta IPs conectados a muitas contas.

        Complexidade de tempo: O(V + E)
        Complexidade de espaço: O(V)
        """
        ip_connections = {}

        for origin in self.graph.get_vertices():
            for destination in self.graph.get_neighbors(origin):
                edge_data = self.graph.get_edge_data(origin, destination)

                if edge_data.get("relation") == "acesso_ip":
                    if destination not in ip_connections:
                        ip_connections[destination] = []

                    ip_connections[destination].append(origin)

        alerts = []

        for ip, accounts in ip_connections.items():
            if len(accounts) >= threshold:
                alerts.append(
                    {
                        "tipo": "ip_compartilhado",
                        "ip": ip,
                        "contas": accounts,
                        "quantidade_contas": len(accounts),
                        "mensagem": "O IP {} está vinculado a múltiplas contas.".format(ip),
                    }
                )

        return alerts

    def detect_high_value_transactions(self, threshold=10000):
        """
        Detecta transações com valor maior ou igual ao limite definido.

        Complexidade de tempo: O(E)
        Complexidade de espaço: O(A), onde A é a quantidade de alertas.
        """
        alerts = []

        for origin, destination, data in self.graph.get_edges():
            if data.get("relation") != "transacao":
                continue

            value = data.get("value")

            if value is None:
                continue

            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                continue

            if numeric_value >= threshold:
                alerts.append(
                    {
                        "tipo": "transacao_alto_valor",
                        "origem": origin,
                        "destino": destination,
                        "valor": numeric_value,
                        "mensagem": (
                            "Transação de alto valor identificada: {} -> {} no valor de R$ {}."
                        ).format(origin, destination, format_currency_br(numeric_value)),
                    }
                )

        return alerts

    def run_analysis(self):
        """
        Executa todas as regras de análise do MVP.
        """
        alerts = []
        alerts.extend(self.detect_high_out_degree_accounts(threshold=3))
        alerts.extend(self.detect_shared_ip_patterns(threshold=3))
        alerts.extend(self.detect_high_value_transactions(threshold=10000))

        return alerts
