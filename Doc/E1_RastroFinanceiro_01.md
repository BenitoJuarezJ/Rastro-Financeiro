# E1 — Proposta e Definição do Projeto
> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 19 de março de 2026  
> **Peso:** 10% da nota final  
---
## Identificação do Grupo
| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Rastro Financeiro — Mapeamento de Fraudes em Redes de Transações |
| Integrante 1 | Benito Juarez Jesus Viana Aguiar — 42750504 |
| Integrante 2 | Guilherme De Andrade Moura — 37123360 |
| Integrante 3 | Lucas Teixeira de Souza — 40131211 |
| Domínio de aplicação | Finanças / segurança de transações |
---
## 1. Contexto e Motivação
No setor financeiro, o número de transações realizadas todos os dias é muito grande, o que dificulta a identificação de comportamentos suspeitos apenas por análises comuns em tabelas ou registros separados. Em muitos casos, a fraude não aparece de forma isolada, mas por meio de conexões entre contas, CPFs, dispositivos e endereços IP que, quando observados separadamente, parecem normais.
Esse cenário se torna ainda mais delicado porque atividades ilícitas costumam explorar justamente essas relações escondidas. Uma conta pode parecer legítima sozinha, mas se ela compartilha o mesmo CPF com outras contas, utiliza o mesmo IP de acessos anteriores ou participa de uma sequência incomum de transferências, já passa a fazer parte de um padrão que merece atenção.
Nesse contexto, a Teoria dos Grafos se apresenta como uma abordagem adequada para organizar e visualizar essas conexões. Em vez de olhar apenas para uma transação por vez, o sistema passa a enxergar a rede completa de relacionamentos, facilitando a identificação de padrões suspeitos e apoiando a prevenção de fraudes financeiras.
---
## 2. Objetivo Geral
Desenvolver um modelo de detecção de fraudes financeiras baseado em grafos, capaz de identificar padrões suspeitos em redes de transações, 
como compartilhamento de CPF, reutilização de endereço IP e conexões incomuns entre contas.
---
## 3. Objetivos Específicos
- [ ] Modelar contas, CPFs, endereços IP e transações como elementos de um grafo  
- [ ] Representar relações entre essas entidades por meio de arestas  
- [ ] Identificar contas conectadas por dados em comum, como CPF ou IP  
- [ ] Detectar padrões suspeitos de movimentação financeira dentro da rede  
- [ ] Apoiar a análise de possíveis atividades ilícitas com base na estrutura do grafo  
---
## 4. Público-Alvo / Caso de Uso Principal
O projeto é voltado para instituições financeiras, fintechs e sistemas de monitoramento de risco que precisam identificar indícios de fraude 
de forma mais rápida e precisa.  
Um exemplo de uso seria a análise de várias contas que, aparentemente, pertencem a pessoas diferentes, mas compartilham o mesmo CPF cadastrado 
ou realizam acessos frequentes pelo mesmo endereço IP.  
Outro caso seria uma sequência de transferências entre contas recém-criadas, formando um padrão circular ou concentrado em poucos nós da rede. 
Com a modelagem em grafos, essas relações deixam de ser vistas de forma isolada e passam a ser observadas como parte de uma estrutura maior, o 
que facilita a investigação de comportamentos anormais.
---
## 5. Justificativa Técnica — Por que Grafos?
A modelagem em grafos é adequada para esse problema porque fraudes financeiras geralmente envolvem relações entre múltiplos elementos, e não apenas eventos independentes.  
Nesse contexto, os **vértices** podem representar contas bancárias, usuários, CPFs, endereços IP e até dispositivos utilizados no acesso. As **arestas** representam vínculos entre esses elementos, como login, cadastro, transferência ou compartilhamento de informação.  
Essa estrutura permite identificar agrupamentos suspeitos, conexões indiretas e padrões que seriam difíceis de perceber em tabelas tradicionais. Por exemplo, se várias contas diferentes estiverem ligadas ao mesmo CPF ou ao mesmo IP, o grafo evidencia essa concentração de conexões.  
Da mesma forma, transferências sucessivas entre contas interligadas podem indicar tentativas de ocultação de origem de valores. Assim, o uso da Teoria dos Grafos se mostra coerente com o problema proposto e tecnicamente adequado para representar redes complexas de transações financeiras.
---
## 6. Tipo de Grafo
| Característica | Escolha | Justificativa breve |
|----------------|---------|---------------------|
| Dirigido ou não-dirigido | Dirigido | Transferências e acessos possuem origem e destino |
| Ponderado ou não-ponderado | Ponderado | Pode representar quantidade de transações, frequência ou valor movimentado |
| Conectado / bipartido / geral | Geral | Há diferentes tipos de entidades e múltiplas relações possíveis |
| Representação interna pretendida | Lista de adjacência | Mais eficiente para redes extensas e esparsas |
---
## 7. Diagrama Conceitual
```text
      [Conta A] --------(usa)-------- [CPF 123]
          |                               |
          |                               |
     (acessa)                         (liga)
          |                               |
       [IP X] --------(acessa)------- [Conta B]
          |                               |
          |                               |
     (transfere) --------------------> [Conta C]
```
### Interpretação
- Conta A e Conta B compartilham o mesmo CPF ou o mesmo IP  
- Conta B e Conta C apresentam movimentações conectadas  
- O sistema pode sinalizar:
  - reutilização suspeita de dados cadastrais  
  - acessos concentrados em um mesmo IP  
  - rede de transações com comportamento incomum  
---
**Legenda:**  
- Nós → contas, CPF, IP e demais entidades financeiras  
- Arestas → vínculos de acesso, cadastro ou transação  
---
## Checklist de Entrega
- [X] Texto entre 300 e 600 palavras (seções 1 a 5)  
- [X] Todos os campos da tabela de identificação preenchidos  
- [X] Tipo de grafo especificado com justificativa  
- [X] Diagrama presente e referenciado no texto  
- [X] Arquivo nomeado como `E1_RastroFinanceiro_01.md`  
---
*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*