class FraudDetector:
            if len(neighbors) >= threshold:
                alerts.append({
                    "tipo": "alto_grau_saida",
                    "vertice": vertex,
                    "quantidade_conexoes": len(neighbors),
                    "mensagem": f"{vertex} possui muitas conexões de saída."
                })

        return alerts

    def detect_shared_ip_patterns(self, threshold=3):
        """
        Detecta IPs conectados a muitas contas.

        Observação importante:
        IP compartilhado pode gerar falso positivo, pois empresas, faculdades
        e redes públicas podem ter muitos usuários no mesmo endereço.

        Por isso, usamos threshold para reduzir ruído.

        Complexidade: O(V + E), pois analisa vértices e relações.
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
                alerts.append({
                    "tipo": "ip_compartilhado",
                    "ip": ip,
                    "contas": accounts,
                    "quantidade_contas": len(accounts),
                    "mensagem": f"O IP {ip} está vinculado a múltiplas contas."
                })

        return alerts

    def run_analysis(self):
        """
        Executa a análise principal do MVP.

        Junta diferentes regras simples para gerar um relatório inicial.
        """
        alerts = []
        alerts.extend(self.detect_high_out_degree_accounts(threshold=3))
        alerts.extend(self.detect_shared_ip_patterns(threshold=3))

        return alerts