import argparse


def main():
    """
    Ponto de entrada do MVP.

    Fluxo:
    1. Usuário informa o arquivo JSON.
    2. Sistema monta o grafo dirigido.
    3. Sistema executa uma BFS a partir do vértice inicial.
    4. Sistema executa regras simples de detecção de suspeitas.
    5. Resultado aparece no terminal.
    """

    parser = argparse.ArgumentParser(
        description="Rastro Financeiro — MVP de detecção de padrões suspeitos em grafos."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Caminho do arquivo JSON com o grafo de transações."
    )

    parser.add_argument(
        "--start",
        required=False,
        help="Vértice inicial para executar BFS. Exemplo: conta_001"
    )

    args = parser.parse_args()

    graph = read_graph_from_json(args.input)

    print("=" * 60)
    print("RASTRO FINANCEIRO — MVP")
    print("Análise de padrões suspeitos em redes de transações")
    print("=" * 60)

    print(f"\nTotal de vértices carregados: {len(graph.get_vertices())}")

    if args.start:
        bfs_result = bfs(graph, args.start)
        print("\nResultado da BFS:")
        print(" -> ".join(bfs_result) if bfs_result else "Nenhuma conexão encontrada.")

    detector = FraudDetector(graph)
    alerts = detector.run_analysis()

    print("\nAlertas encontrados:")

    if not alerts:
        print("Nenhum padrão suspeito identificado com os thresholds atuais.")
    else:
        for index, alert in enumerate(alerts, start=1):
            print(f"\nAlerta {index}")
            print(f"Tipo: {alert['tipo']}")
            print(f"Mensagem: {alert['mensagem']}")

            if "vertice" in alert:
                print(f"Vértice: {alert['vertice']}")
                print(f"Quantidade de conexões: {alert['quantidade_conexoes']}")

            if "ip" in alert:
                print(f"IP: {alert['ip']}")
                print(f"Contas relacionadas: {', '.join(alert['contas'])}")

    print("\nAnálise finalizada.")


if __name__ == "__main__":
    main()