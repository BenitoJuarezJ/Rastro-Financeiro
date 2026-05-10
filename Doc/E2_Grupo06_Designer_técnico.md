# E2 — Design Técnico, Arquitetura e Backlog

**Projeto:** Rastro Financeiro — Mapeamento de Fraudes em Redes de Transações  
**Disciplina:** Teoria dos Grafos  
**Prazo:** 13 de abril de 2026  
**Peso:** 20% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|---|---|
| **Nome do projeto** | Rastro Financeiro — Mapeamento de Fraudes em Redes de Transações |
| **Integrante 1** | Benito Juarez Jesus Viana Aguiar — 42750504 |
| **Integrante 2** | Guilherme De Andrade Moura — 37123360 |
| **Integrante 3** | Lucas Teixeira de Souza — 40131211 |
| **Domínio de aplicação** | Finanças / segurança de transações |

---

## 1. Algoritmos Escolhidos

### 1.1 Algoritmo Principal

### 🔹 Algoritmo 1: Componentes Fortemente Conectados (Algoritmo de Tarjan)

**Categoria:** Busca e Conectividade em Grafos Dirigidos.  
**Complexidade de Tempo:** `O(V + E)`  
**Complexidade de Espaço:** `O(V)`

**Justificativa:**  
No contexto de fraudes financeiras, ciclos de transferências entre contas recém-criadas ou grupos de contas que transacionam intensamente entre si são fortes indícios de lavagem de dinheiro ou *smurfing*. O algoritmo de Tarjan identifica esses agrupamentos fechados de forma eficiente em uma única passagem de busca.

**Comparação com Alternativa:**  
O algoritmo de Kosaraju também encontra componentes conexos, porém exige duas passagens de DFS (uma no grafo original e outra no transposto), sendo menos eficiente em termos de tempo para grandes volumes de transações em tempo real.

**Limitações:**  
Não identifica fraudes que ocorrem em caminhos lineares simples, apenas em estruturas cíclicas ou altamente interligadas.

**Referência:**  
SEDGEWICK, R.; WAYNE, K. *Algorithms*. 4. ed. Upper Saddle River: Addison-Wesley, 2011.

---

### 🔹 Algoritmo 2: Busca em Largura (BFS) com Detecção de Multicamadas

**Categoria:** Busca em Grafos.  
**Complexidade de Tempo:** `O(V + E)`  
**Complexidade de Espaço:** `O(V)`

**Justificativa:**  
Essencial para identificar contas que compartilham o mesmo CPF ou endereço IP. Ao partir de um nó "CPF", o BFS revela rapidamente todas as contas conectadas a ele (vizinhança de 1º nível) e quais outras entidades essas contas acessaram (2º nível), expondo a rede de rastro financeiro.

**Comparação com Alternativa:**  
Busca em Profundidade (DFS). A DFS poderia se aprofundar demais em uma única cadeia de transferências, enquanto a detecção de fraude exige uma visão radial (quem está em volta deste IP agora?), para a qual a BFS é superior.

**Limitações:**  
Em grafos com nós de altíssimo grau (ex.: um IP público de uma grande empresa), a BFS pode gerar muitos falsos positivos.

**Referência:**  
CORMEN, T. H. et al. *Algoritmos: Teoria e Prática*. 3. ed. Rio de Janeiro: Elsevier, 2012.

---

## 2. Arquitetura em Camadas

O sistema segue o padrão de separação de responsabilidades para garantir manutenibilidade:

- **Apresentação (UI/CLI):** Interface via console onde o analista insere um CPF, Conta ou IP suspeito e recebe o relatório de conexões e riscos detectados.
- **Aplicação (Service):** Camada que gerencia a lógica de negócio, como definir o que é considerado um "alerta de fraude" e coordenar os algoritmos.
- **Domínio (Core):** Implementação da estrutura de dados do grafo (Lista de Adjacência) e os algoritmos de Tarjan e BFS.
- **Infraestrutura (I/O):** Módulo de persistência que realiza a leitura dos logs de transações e cadastros em formato JSON.

---

## 3. Estrutura de Diretórios

```text
.
├── .github/
│   └── instructions/
│       └── codacy.instructions.md
│
├── .vscode/
│   └── settings.json
│
├── rastro-financeiro/
│   ├── doc/                  # Documentação (E1 e E2)
│   ├── data/                 # Datasets JSON de transações
│   ├── src/
│   │   ├── ui/               # Camada de Apresentação
│   │   ├── service/          # Camada de Aplicação
│   │   ├── core/             # Algoritmos e Grafos (Domínio)
│   │   └── infra/            # Leitor de arquivos (Infraestrutura)
│   └── main.py               # Ponto de entrada
│
├── .gitignore
├── README.md
└── LICENSE
```

**Justificativa:**  
A estrutura segue fielmente o modelo solicitado, separando a inteligência algorítmica (`core`) da entrada de dados (`infra`).

**Justificativa de desvios (se houver):**  
Não há desvios declarados.

---

## 4. Definição do Dataset

**Formato:** JSON.

**Estratégia de Geração:**  
Geração de grafos aleatórios variando o número de vértices (contas/CPFs) e densidade de arestas (transações).

**Parâmetros:**  
- `n_vertices` entre 50 e 500  
- `probabilidade_conexao` para simular redes esparsas  

**Exemplo de Schema:**

```json
{
  "entidades": [
    { "id": "C1", "tipo": "CONTA" },
    { "id": "CPF_123", "tipo": "CPF" },
    { "id": "IP_X", "tipo": "IP" }
  ],
  "relacoes": [
    { "origem": "C1", "destino": "CPF_123", "tipo": "USA", "peso": 1 },
    { "origem": "C1", "destino": "IP_X", "tipo": "ACESSA", "peso": 5 },
    { "origem": "C1", "destino": "C2", "tipo": "TRANSFERE", "valor": 5000 }
  ]
}
```

---

## 5. Backlog do Projeto

### 5.1 In-Scope — O que será implementado

- **Carga de Rede Financeira:** Dado um arquivo JSON de transações, quando o sistema for iniciado, então deve construir um grafo dirigido e ponderado em memória.
- **Identificação de Contas por CPF:** Dado um CPF suspeito, quando consultado via BFS, então o sistema deve listar todas as contas vinculadas a ele.
- **Detecção de Ciclos Suspeitos:** Dado o conjunto de transações, quando executado o algoritmo de Tarjan, então o sistema deve sinalizar grupos de contas com transferências circulares.
- **Alerta de IP Compartilhado:** Dado um endereço IP, quando acessado por mais de 3 contas diferentes, então o sistema deve gerar um alerta de risco alto.
- **Relatório de Rastro:** Dado um ID de transação, quando processado, então o sistema deve exibir o caminho completo do dinheiro em menos de 1 segundo.

### 5.2 Out-of-Scope — O que NÃO será feito

- **Monitoramento Real-Time:** O sistema processará lotes (*batch*) de arquivos, não fluxos contínuos.
- **Bloqueio Automático de Contas:** O sistema apenas sinaliza fraudes para análise humana, não executa bloqueios em APIs bancárias.
- **Interface Web:** O projeto será estritamente CLI (linha de comando).

---

## Checklist de Entrega

- [x] **Big-O de tempo e espaço declarados para cada algoritmo**  
  Tarjan: Tempo `O(V + E)` e Espaço `O(V)`.  
  BFS: Tempo `O(V + E)` e Espaço `O(V)`.

- [x] **Ao menos 1 alternativa descartada com justificativa**  
  Descartado: Algoritmo de Kosaraju, pois exige duas passagens de DFS e transposição do grafo, sendo menos eficiente que o Tarjan para alta volumetria.

- [x] **Diagrama de arquitetura com 4 camadas identificadas**  
  Apresentação (CLI): Entrada de IDs.  
  Aplicação: Regras de risco.  
  Domínio: Grafo e Algoritmos.  
  Infraestrutura: Parser JSON.

- [x] **Referência bibliográfica para cada algoritmo (ABNT ou IEEE)**  
  CORMEN, T. H. et al. *Algoritmos: Teoria e Prática*. 3. ed. 2012.  
  SEDGEWICK, R. *Algorithms*. 4. ed. 2011.

- [x] **Backlog com ≥ 5 itens In-Scope e ≥ 3 Out-of-Scope**  
  In-Scope: Loader JSON, Grafo (Adjacência), Tarjan (Ciclos), BFS (Vizinhança), Relatório.  
  Out-of-Scope: GUI, Tempo Real, Bloqueio de Contas.

- [x] **Ao menos 3 critérios de aceite no formato "dado / quando / então"**  
  **C1:** Dado um ciclo de 3 contas, quando o Tarjan rodar, então o sistema deve identificar o Componente Fortemente Conectado.  
  **C2:** Dado um IP suspeito, quando a BFS for executada, então o sistema deve listar todos os CPFs vinculados a ele.  
  **C3:** Dado um grafo de 1.000 nós, quando processado, então a resposta deve ser gerada em menos de 1 segundo.

- [x] **Exemplo de estrutura de arquivo de entrada presente**

```json
{
  "vertices": [
    { "id": "C1", "tipo": "CONTA" }
  ],
  "arestas": [
    { "origem": "C1", "destino": "IP1", "tipo": "ACESSA" }
  ]
}
```

---

**Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai**
