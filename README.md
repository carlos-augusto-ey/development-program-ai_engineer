# Programa de Formação – Engenheiro de IA 🤖

**IA Generativa, Agentes Inteligentes e Engenharia de Software para Produção**

## Visão Geral

Bem-vindo ao repositório do **Programa de Formação para Engenheiros de IA**. Nossa filosofia é simples: **não criamos protótipos, construímos soluções**. Este programa foi desenhado para preparar profissionais para atuar em desafios reais de IA generativa em ambiente corporativo, com foco em arquiteturas escaláveis, agentes inteligentes e engenharia de sistemas prontos para performar.

O objetivo é ir além do código, conectando decisões técnicas a um impacto de negócio mensurável.

## 🎯 Público-Alvo

Este programa é ideal para **engenheiros de software, dados ou back-end com experiência em Python** que desejam se especializar na construção de sistemas de IA generativa de ponta a ponta, desde a concepção até a preparação para o ambiente de produção.

## 💡 Nossa Metodologia: O Ciclo de Maestria em IA

Adotamos um ciclo de aprendizado ativo para garantir um desenvolvimento profundo e multifacetado.

-   **Aprender (Learn):** Focar nos conceitos teóricos com o suporte do nosso *Learning Path* e da documentação oficial. O objetivo é entender o "porquê" por trás de cada tecnologia.
-   **Construir (Build):** Aplicar o conhecimento na prática, desenvolvendo os três projetos principais. Aqui, a teoria se transforma em código funcional e soluções tangíveis.
-   **Apresentar (Present):** Criar artefatos que demonstrem o valor da solução, como a interface interativa com Streamlit. A capacidade de apresentar o trabalho é crucial.
-   **Defender (Defend):** Justificar as escolhas técnicas e de arquitetura nos documentos de decisão (`docs/decisions.md`). Esta é a habilidade de um engenheiro sênior: comunicar e defender suas soluções com base em fundamentos sólidos.

## 🚀 A Jornada do Engenheiro de IA

Este programa é uma jornada de transformação. O participante evolui de um engenheiro de software ou dados para um arquiteto de soluções de IA, dominando novas ferramentas e conceitos a cada etapa.

```mermaid
graph TD
    subgraph "Ponto de Partida"
        A[Engenheiro de<br>Software/Dados]
    end

    subgraph "Projeto 1: API Inteligente"
        B(API Inteligente Produtizada)
        B_Techs["- Python & FastAPI<br>- Pydantic Schemas<br>- Prompt Engineering<br>- Docker"]
    end

    subgraph "Projeto 2: RAG Confiável"
        C(RAG Confiável com Re-ranking)
        C_Techs["- Vector DBs<br>- Chunking Semântico<br>- Retrieval & Re-ranking<br>- Grounding"]
    end

    subgraph "Projeto 3: Agente Autônomo"
        D(Agente Inteligente para Automação)
        D_Techs["- LangGraph<br>- Orquestração Multi-step<br>- Tool Calling<br>- LLMOps (Observabilidade)"]
    end

    subgraph "Ponto de Chegada"
        E[Engenheiro de IA<br>Full-Stack]
    end

    A --> B --> C --> D --> E
    B --- B_Techs
    C --- C_Techs
    D --- D_Techs

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
```

## 🏅 O Perfil do Engenheiro de IA Moderno

Ao final do programa, o participante estará apto a atuar como um Engenheiro de IA completo, dominando habilidades técnicas e comportamentais.

### Hard Skills Desenvolvidas
- **Desenvolvimento de Backend:** Construção de APIs robustas com Python, FastAPI e Pydantic.
- **Arquitetura de IA:** Design e implementação de sistemas RAG, incluindo ingestão, indexação e recuperação otimizada.
- **Agentes Autônomos:** Orquestração de fluxos de trabalho complexos com LangGraph, gerenciamento de estado e uso de ferramentas.
- **Engenharia de Software:** Conteinerização com Docker, escrita de testes e documentação técnica.
- **LLMOps & Observabilidade:** Instrumentação de código para monitoramento de performance, custo e comportamento de sistemas de IA em produção.

### Soft Skills Essenciais
- **Resolução de Problemas:** Capacidade de traduzir uma dor de negócio em uma solução de IA viável e eficaz.
- **Pensamento Crítico:** Análise de trade-offs entre diferentes abordagens técnicas (ex: qual a melhor estratégia de chunking para este caso?).
- **Comunicação Técnica:** Habilidade de apresentar e defender decisões de arquitetura de forma clara e concisa.
- **Visão de Produto:** Foco em construir soluções que não apenas funcionam, mas que geram valor de negócio mensurável.

## 🗂️ Guia Rápido dos Projetos

Use a tabela abaixo para navegar diretamente para o guia de cada projeto.

| Fase do Programa | Objetivo do Projeto | Link Direto para o Guia |
| :--- | :--- | :--- |
| **Projeto 1** | Construir uma API REST com LLM | [**Guia do Projeto 1**](./projects/project-1/README.md) |
| **Projeto 2** | Adicionar uma base de conhecimento (RAG) | [**Guia do Projeto 2**](./projects/project-2/README.md) |
| **Projeto 3** | Automatizar o fluxo com um Agente | [**Guia do Projeto 3**](./projects/project-3/README.md) |

## 🚦 Como Começar a Desenvolver

1.  **Acesse a pasta do Projeto 1:** `cd projects/project-1`.
2.  **Siga as instruções** no `README.md` dentro da pasta para configurar o ambiente e começar a desenvolver.
3.  Ao concluir o Projeto 1, você continuará a evoluir o código que você mesmo criou para o Projeto 2, e assim por diante.

> **Dica:** A melhor abordagem é criar seu próprio repositório Git e copiar a estrutura de pastas de `projects/project-1` para lá. Assim, você constrói sua própria versão da solução do zero.

---

## 🔗 Recursos e Documentação (Learning Path)

Para se aprofundar nos conceitos que veremos, consulte as documentações oficiais:

- **Python:** [Documentação Oficial do Python 3](https://docs.python.org/3/)
- **FastAPI:** [Tutorial do FastAPI](https://fastapi.tiangolo.com/tutorial/) - Essencial para os Projetos 1 e 2.
- **Pydantic:** [Documentação do Pydantic V2](https://docs.pydantic.dev/latest/) - Fundamental para validação de dados.
- **Docker:** [Visão Geral do Docker](https://docs.docker.com/get-started/overview/)
- **LangChain:** [Documentação da LangChain para Python](https://python.langchain.com/docs/get_started/introduction) - Base para os Projetos 2 e 3.
- **LangGraph:** [Introdução ao LangGraph](https://langchain-ai.github.io/langgraph/) - O coração do nosso agente no Projeto 3.
- **Streamlit:** [Documentação do Streamlit](https://docs.streamlit.io/) - Para a criação da interface de demonstração.
- **OpenTelemetry:** [Documentação do OpenTelemetry](https://opentelemetry.io/docs/) - Para o desafio de observabilidade.


