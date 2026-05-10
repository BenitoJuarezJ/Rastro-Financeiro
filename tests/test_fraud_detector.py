from src.core.graph import DirectedGraph
from src.services.fraud_detector import FraudDetector


def test_detect_shared_ip_patterns():
    graph = DirectedGraph()
    graph.add_edge("conta_001", "ip_1", relation="acesso_ip")
    graph.add_edge("conta_002", "ip_1", relation="acesso_ip")
    graph.add_edge("conta_003", "ip_1", relation="acesso_ip")

    detector = FraudDetector(graph)
    alerts = detector.detect_shared_ip_patterns(threshold=3)

    assert len(alerts) == 1
    assert alerts[0]["tipo"] == "ip_compartilhado"


def test_no_shared_ip_below_threshold():
    graph = DirectedGraph()
    graph.add_edge("conta_001", "ip_1", relation="acesso_ip")
    graph.add_edge("conta_002", "ip_1", relation="acesso_ip")

    detector = FraudDetector(graph)
    alerts = detector.detect_shared_ip_patterns(threshold=3)

    assert alerts == []


def test_high_out_degree_account():
    graph = DirectedGraph()
    graph.add_edge("conta_001", "conta_002")
    graph.add_edge("conta_001", "conta_003")
    graph.add_edge("conta_001", "conta_004")

    detector = FraudDetector(graph)
    alerts = detector.detect_high_out_degree_accounts(threshold=3)

    assert len(alerts) == 1
    assert alerts[0]["vertice"] == "conta_001"


def test_high_value_transaction():
    graph = DirectedGraph()
    graph.add_edge("conta_001", "conta_002", relation="transacao", value=15000)

    detector = FraudDetector(graph)
    alerts = detector.detect_high_value_transactions(threshold=10000)

    assert len(alerts) == 1
    assert alerts[0]["tipo"] == "transacao_alto_valor"
