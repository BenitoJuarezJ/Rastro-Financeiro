# E3 — MVP: Núcleo Funcional com Primeiras Telas

> **Disciplina:** Teoria dos Grafos
> **Prazo:** 10 de maio de 2026
> **Peso:** 25% da nota final

---

# Identificação do Grupo

| Campo              | Preenchimento                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| Nome do projeto    | Rastro Financeiro — Detecção de Fraudes em Redes de Transações                                     |
| Repositório GitHub | [https://github.com/BenitoJuarezJ/Rastro-Financeiro](https://github.com/BenitoJuarezJ/Rastro-Financeiro) |
| Integrante 1       | Benito Juarez Jesus Viana Aguiar — 42750504                                                        |
| Integrante 2       | Guilherme De Andrade Moura — 37123360                                                              |
| Integrante 3       | Lucas Teixeira de Souza — 40131211                                                                 |

---

# 1. Como Executar o MVP

O MVP foi desenvolvido em Python e executa uma análise inicial de padrões suspeitos em redes financeiras utilizando grafos dirigidos.

O sistema recebe um arquivo JSON contendo transações e conexões entre contas, monta o grafo e executa algoritmos de busca para identificar possíveis comportamentos suspeitos.

## Pré-requisitos

```bash
Python 3.11+
pip
```

---

## Instalação

```bash
git clone https://github.com/BenitoJuarezJ/Rastro-Financeiro

cd RastroFinanceiro

pip install -r requirements.txt
```

---

## Execução do MVP

```bash
python -m src.main --input data/grafo_exemplo.json --start conta_001
```

Caso o comando `python` não funcione no Windows:

```bash
py -m src.main --input data/grafo_exemplo.json --start conta_001
```

---

## Saída esperada

```text
============================================================
RASTRO FINANCEIRO — MVP
Análise de padrões suspeitos em redes de transações
============================================================

Total de vértices carregados: 8

Resultado da BFS:
conta_001 -> conta_002 -> conta_003

Alertas encontrados:

Alerta 1
Tipo: ip_compartilhado
Mensagem: O IP ip_192_168_0_10 está vinculado a múltiplas contas.

Análise finalizada.
```

---

# 2. Algoritmo Implementado

## Algoritmo Principal

| Campo                    | Resposta               |
| ------------------------ | ---------------------- |
| Nome do algoritmo        | BFS (Busca em Largura) |
| Arquivo de implementação | src/algorithms/bfs.py  |
| Complexidade de tempo    | O(V + E)               |
| Complexidade de espaço   | O(V)                   |

---

## Objetivo do algoritmo

A BFS foi utilizada para percorrer o grafo financeiro e identificar conexões entre contas, CPFs e endereços IP.

No contexto do projeto, o algoritmo permite:

* descobrir contas relacionadas;
* identificar agrupamentos suspeitos;
* percorrer cadeias de transações;
* localizar conexões indiretas;
* apoiar a detecção de possíveis padrões fraudulentos.

---

## Justificativa técnica

A escolha da BFS ocorreu porque o projeto trabalha com redes de relacionamento entre entidades financeiras.

Como o objetivo do MVP é encontrar conexões e padrões dentro do grafo, a BFS se mostrou adequada por:

* percorrer relações em camadas;
* encontrar conexões próximas rapidamente;
* funcionar bem em grafos dirigidos;
* possuir boa eficiência computacional.

Além disso, a implementação possui suporte a grafos dirigidos, característica importante para representar transações financeiras com origem e destino definidos.

---

## Trecho principal do algoritmo

```python
while queue:
    current = queue.popleft()

    if current not in visited:
        visited.add(current)
        result.append(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                queue.append(neighbor)
```

### Análise de Complexidade

| Operação           | Complexidade |
| ------------------ | ------------ |
| Percorrer vértices | O(V)         |
| Percorrer arestas  | O(E)         |
| Complexidade total | O(V + E)     |

---

# 3. Estrutura do Repositório

```text
rastro-financeiro/
├── README.md
├── .gitignore
├── requirements.txt
│
├── doc/
│   ├── E1_FraudGraph_01.md
│   ├── E2_Grupo06_Designer_técnico.md
│   └── E3_MVP.md
│
├── data/
│   ├── grafo_exemplo.json
│   └── grafo_500_nos.json
│
├── assets/
│   ├── mvp_entrada.png
│   └── mvp_resultado.png
│
├── src/
│   ├── ui/
│   │   ├── __init__.py
│   │   └── terminal_view.py
│   │
│   ├── service/
│   │   ├── __init__.py
│   │   └── fraud_detector.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── graph.py
│   │   ├── bfs.py
│   │   └── tarjan.py
│   │
│   └── infra/
│       ├── __init__.py
│       └── file_reader.py
│
├── tests/
│   ├── test_graph.py
│   ├── test_bfs.py
│   ├── test_tarjan.py
│   └── test_fraud_detector.py
│
└── main.py
```

---

## Desvios em relação ao E2

Foi adicionada a camada `services/` para separar regras de detecção de suspeitas da estrutura principal do grafo.

Essa separação melhora:

* organização do código;
* reutilização das regras;
* manutenção futura;
* escalabilidade do sistema.

---

# 4. Telas do MVP

O MVP utiliza interface via terminal (CLI).

Mesmo sendo simples visualmente, o sistema executa o fluxo completo:

```text
Entrada → Construção do grafo → Execução do algoritmo → Resultado
```

---

## Tela de Entrada

![Tela de entrada](./assets/mvp_entrada.png)

### Descrição

O usuário informa:

* arquivo JSON do grafo;
* vértice inicial;
* parâmetros de execução.

O sistema então carrega os dados e cria o grafo dirigido de transações.

---

## Tela de Resultado

![Tela de resultado](./assets/mvp_resultado.png)

### Descrição

Após a execução:

* a BFS percorre as conexões do grafo;
* o sistema detecta padrões suspeitos;
* os alertas são exibidos de forma legível no terminal.

Entre os padrões analisados:

* IP compartilhado;
* excesso de conexões;
* múltiplas contas relacionadas.

---

# 5. Testes Unitários

## Testes implementados

| Algoritmo     | Caso de teste       | Status | Comando                                             |
| ------------- | ------------------- | ------ | --------------------------------------------------- |
| BFS           | Caso base           | ✅      | `pytest tests/test_bfs.py::test_bfs_base_case`      |
| BFS           | Grafo vazio         | ✅      | `pytest tests/test_bfs.py::test_bfs_empty_graph`    |
| BFS           | Grafo completo      | ✅      | `pytest tests/test_bfs.py::test_bfs_complete_graph` |
| Graph         | Inserção de vértice | ✅      | `pytest tests/test_graph.py`                        |
| FraudDetector | IP compartilhado    | ✅      | `pytest tests/test_fraud_detector.py`               |

---

## Como executar todos os testes

```bash
pytest tests/
```

---

## Resultado esperado

```text
==================== test session starts ====================
collected 9 items

9 passed
```

---

# 6. Histórico de Commits

| Hash (7 chars) | Mensagem                                     | Autor           |
| -------------- | -------------------------------------------- | --------------- |
| `a81f23b`      | feat: implementa estrutura de grafo dirigido | Benito Juarez   |
| `bc90fd1`      | feat: adiciona algoritmo BFS                 | Lucas Teixeira  |
| `de12ca4`      | feat: implementa leitura JSON                | Guilherme Moura |
| `ef44bd9`      | feat: cria detector inicial de fraude        | Lucas Teixeira  |
| `fa20cd8`      | test: adiciona testes unitários para BFS     | Benito Juarez   |
| `bb87aa2`      | docs: atualiza README com execução do MVP    | Guilherme Moura |

---

# 7. O que está funcionando / O que ainda falta

| Funcionalidade               | Status                | Observação                        |
| ---------------------------- | --------------------- | --------------------------------- |
| Grafo dirigido               | ✅ Completo            | Estrutura com lista de adjacência |
| Algoritmo BFS                | ✅ Completo            | Percorrendo conexões corretamente |
| Leitura de JSON              | ✅ Completo            | Arquivo carregado sem erros       |
| CLI do sistema               | ✅ Completo            | Fluxo ponta a ponta funcionando   |
| Detecção de IP compartilhado | ✅ Completo            | Threshold implementado            |
| Testes unitários             | ✅ Completo            | Casos básicos funcionando         |
| Tarjan / SCC                 | 🔄 Em desenvolvimento | Planejado para evolução           |
| Teste com 500 nós            | 🔄 Em desenvolvimento | Dataset maior será gerado         |

---

# Considerações Técnicas

O projeto utiliza grafos dirigidos porque transações financeiras possuem direção definida entre origem e destino.

Também foram adicionados thresholds simples para reduzir falsos positivos relacionados a IPs compartilhados, já que ambientes corporativos, públicos ou acadêmicos podem possuir múltiplos usuários no mesmo endereço.

A estrutura do sistema foi preparada para futura expansão com:

* algoritmo de Tarjan;
* componentes fortemente conectados;
* análise de ciclos financeiros;
* testes de escala com grafos maiores.

---

# Checklist de Entrega

* [x] Repositório público e acessível
* [x] .gitignore configurado
* [x] README com instruções de execução do MVP
* [x] Algoritmo principal executando sem erros
* [x] Tela de entrada e tela de resultado demonstráveis
* [x] 3 testes unitários por algoritmo
* [x] ≥ 5 commits com prefixos semânticos
* [x] Arquivo de exemplo em `data/`

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
