import argparse
import sys
from pathlib import Path

# Permite executar o arquivo com:
# python src/main.py
# python -m src.main
# python main.py
if __package__ is None or __package__ == "":
    project_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(project_root))

from src.algorithms.bfs import bfs
from src.io.file_reader import GraphFileError, read_graph_from_json
from src.services.fraud_detector import FraudDetector, format_currency_br


def build_parser():
    parser = argparse.ArgumentParser(
        description="Rastro Financeiro — MVP de detecção de padrões suspeitos em grafos."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Caminho do arquivo JSON com o grafo de transações.",
    )

    parser.add_argument(
        "--start",
        required=False,
        help="Vértice inicial para executar BFS. Exemplo: conta_001",
    )

    return parser


def print_alert(alert, index):
    print("\nAlerta {}".format(index))
    print("Tipo: {}".format(alert["tipo"]))
    print("Mensagem: {}".format(alert["mensagem"]))

    if "vertice" in alert:
        print("Vértice: {}".format(alert["vertice"]))
        print("Quantidade de conexões: {}".format(alert["quantidade_conexoes"]))

    if "ip" in alert:
        print("IP: {}".format(alert["ip"]))
        print("Contas relacionadas: {}".format(", ".join(alert["contas"])))
        print("Quantidade de contas: {}".format(alert["quantidade_contas"]))

    if "origem" in alert and "destino" in alert:
        print("Origem: {}".format(alert["origem"]))
        print("Destino: {}".format(alert["destino"]))
        print("Valor: R$ {}".format(format_currency_br(alert["valor"])))


def main():
    """
    Ponto de entrada do MVP.

    Fluxo:
    1. Usuário informa o arquivo JSON.
    2. Sistema monta o grafo dirigido.
    3. Sistema executa uma BFS a partir do vértice inicial, quando informado.
    4. Sistema executa regras simples de detecção de suspeitas.
    5. Resultado aparece no terminal.
    """
    parser = build_parser()
    args = parser.parse_args()

    try:
        graph = read_graph_from_json(args.input)
    except GraphFileError as error:
        print("Erro ao carregar o grafo: {}".format(error), file=sys.stderr)
        sys.exit(1)

    print("=" * 60)
    print("RASTRO FINANCEIRO — MVP")
    print("Análise de padrões suspeitos em redes de transações")
    print("=" * 60)

    print("\nTotal de vértices carregados: {}".format(graph.number_of_vertices()))
    print("Total de arestas carregadas: {}".format(graph.number_of_edges()))

    if args.start:
        bfs_result = bfs(graph, args.start)
        print("\nResultado da BFS:")

        if bfs_result:
            print(" -> ".join(bfs_result))
        else:
            print("Nenhuma conexão encontrada.")

    detector = FraudDetector(graph)
    alerts = detector.run_analysis()

    print("\nAlertas encontrados:")

    if not alerts:
        print("Nenhum padrão suspeito identificado com os thresholds atuais.")
    else:
        for index, alert in enumerate(alerts, start=1):
            print_alert(alert, index)

    print("\nAnálise finalizada.")


if __name__ == "__main__":
    main()
