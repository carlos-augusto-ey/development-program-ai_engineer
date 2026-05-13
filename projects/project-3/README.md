# Projeto 3 – Agentes Inteligentes e Automação de Processos

**Objetivo:** Construir um agente autônomo que orquestra o processo de análise de conformidade de ponta a ponta, automatizando tarefas manuais e fornecendo indicadores claros de eficiência.

---

## 📝 Cenário de Negócio (FSO - Financial Services Office)

**A Dor (Final):** Temos uma API RAG poderosa, mas o processo ainda depende de intervenção humana. Alguém precisa pegar as "Minutas de Recomendação", chamar a API e, com base na resposta, decidir o que fazer: arquivar o documento ou escalar para um analista. Isso ainda é um gargalo operacional.

**Nossa Solução (Fase 3):** Vamos construir o **"Compliance Agent"**, um sistema autônomo que assume todo o fluxo de trabalho. Ele irá monitorar a chegada de novos documentos, usar a inteligência que construímos nos projetos anteriores para analisá-los e tomar ações de forma independente, liberando a equipe de compliance para focar apenas nos casos que realmente exigem atenção humana.

## 🛠️ Tecnologias e Conceitos Chave

- **Orquestração de Agentes:** LangChain / LangGraph para modelar o fluxo de trabalho como um grafo de estados.
- **Técnicas de IA:**
  - **Agentes Autônomos:** O núcleo do projeto, um sistema que raciocina e age.
  - **Orquestração de Fluxos Multi-step:** Coordenar uma sequência de tarefas (ler, analisar, decidir, agir).
  - **Tool Retrieval e Tool Calling:** O agente terá "ferramentas" à sua disposição (ex: a API do Projeto 2, uma ferramenta para mover arquivos, uma para criar alertas).
  - **Gerenciamento de Estado (Multi-turn State):** Manter o controle sobre o estado de cada documento sendo processado.
  - **Model Context Protocol (MCP):** Usar um protocolo formal para que os componentes do sistema (orquestrador, ferramentas) se comuniquem de forma estruturada.
  - **Guardrails:** Implementar mecanismos de segurança para garantir que o agente opere dentro de limites seguros.

## ✅ Entregáveis

Para concluir este projeto, você deverá entregar:

1.  **Fluxo de Agentes Funcional:**
    - Um agente que monitora o diretório `data/input/` para novos arquivos de recomendação.
    - O agente deve orquestrar o seguinte fluxo:
      1.  **Detectar** um novo arquivo.
      2.  **Invocar** a análise de conformidade (usando a lógica do Projeto 2).
      3.  **Decidir** com base no resultado (`is_compliant`).
      4.  **Agir:** Mover o arquivo para `data/output/approved` se estiver conforme, ou para `data/output/rejected_for_review` e criar um alerta (simulado em um log) se não estiver.

2.  **Logs e Rastreabilidade de Execução:**
    - O sistema deve gerar logs claros que permitam rastrear cada passo da decisão do agente para um determinado documento.

3.  **Indicador de Automação (Antes vs. Depois):**
    - Um cálculo, documentado no `README` do projeto, que demonstre o ganho de eficiência. Exemplo:
      - **Antes:** 100% de análise manual.
      - **Depois:** 95% de automação, 5% de intervenção manual.
      - **Resultado:** Redução de X horas de trabalho manual por semana.

4.  **Documento de Decisões Arquiteturais:**
    - Uma atualização no `docs/decisions.md` explicando o design do agente, o grafo de estados e os contratos MCP definidos.

## 🚀 Como Começar

1.  **Modele o Grafo:** Usando o LangGraph, desenhe o fluxo de estados do agente: `(start) -> (analyze_document) -> (check_compliance) -> (take_action) -> (end)`.
2.  **Crie as Ferramentas (Tools):**
    - Crie uma "ferramenta" que encapsula a chamada à sua API RAG do Projeto 2.
    - Crie ferramentas simples para interagir com o sistema de arquivos (mover arquivos).
    - Crie uma ferramenta para "criar um alerta" (que pode simplesmente printar no console ou escrever em um arquivo de log).
3.  **Construa o Agente Orquestrador:** Implemente o agente em `src/agents/compliance_agent.py`, conectando o grafo do LangGraph com as ferramentas criadas.
4.  **Implemente o Gatilho (Trigger):** Crie um loop principal em `src/main.py` (ou em um script separado) que monitore o diretório de entrada e dispare o agente para cada novo arquivo.
5.  **Calcule o Indicador:** Execute o agente com um lote de arquivos de teste (alguns conformes, outros não) e calcule a taxa de automação.

---

Este projeto final consolida todo o aprendizado do programa, transformando você de um construtor de componentes de IA para um **arquiteto de sistemas de IA autônomos e orientados a valor**.