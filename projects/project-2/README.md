# Projeto 2 – RAG Confiável com Re-ranking

**Objetivo:** Evoluir a "Compliance Checker API" para um sistema robusto de RAG (Retrieval-Augmented Generation), garantindo que as análises de conformidade sejam baseadas em uma base de conhecimento auditável e de alta qualidade.

---

## 📝 Cenário de Negócio (FSO - Financial Services Office)

**A Dor (Evolução):** A API que construímos no Projeto 1 funciona, mas tem uma limitação crítica: suas regras de negócio estão "congeladas" dentro do prompt. Se uma política de investimento mudar, um desenvolvedor precisa reescrever e reimplantar o código. A análise não é facilmente auditável, pois não podemos apontar para a cláusula exata da política que foi usada.

**Nossa Solução (Fase 2):** Vamos transformar nossa API em um **"Policy-Grounded RAG"**. Antes de pedir ao LLM para analisar uma recomendação, nosso sistema irá primeiro buscar os trechos mais relevantes dos documentos de política (`knowledge_base/`) e os fornecerá como contexto. Isso garante que a decisão seja sempre baseada na documentação oficial e atualizada.

## 🛠️ Tecnologias e Conceitos Chave

- **Backend:** Python 3.11+
- **Bancos de Dados Vetoriais:** Ferramentas como ChromaDB, FAISS, ou serviços de nuvem para armazenar e consultar embeddings.
- **Técnicas de IA:**
  - **Ingestão e Indexação:** O processo de ler, dividir (`chunking`) e vetorizar os documentos da `knowledge_base`.
  - **Chunking Semântico:** Estratégias para dividir os documentos de forma inteligente, preservando o significado.
  - **Filtros de Recuperação:** Técnicas para refinar a busca no banco de dados vetorial.
  - **Strict Grounding:** Forçar o LLM a basear sua resposta exclusivamente no contexto recuperado.
  - **Técnicas de Re-ranking:** Algoritmos para reordenar os resultados da busca, trazendo os mais relevantes para o topo.

## ✅ Entregáveis

Para concluir este projeto, você deverá entregar:

1.  **Pipeline RAG Funcional:**
    - Um script ou serviço de ingestão que processa os documentos da pasta `knowledge_base/` e os armazena em um banco de dados vetorial.
    - A lógica da API do Projeto 1 deve ser modificada para:
      1.  Receber a query.
      2.  Buscar (`retrieve`) o contexto relevante no banco de dados vetorial.
      3.  Injetar o contexto no prompt do LLM.
      4.  Retornar a resposta do LLM, que agora deve incluir a fonte da informação (ex: `source_document: 'politica_adequacao_investimento_v1.2.txt'`).

2.  **Evidência de Melhoria com Re-ranking:**
    - Uma análise (pode ser em um Jupyter Notebook ou em um script de teste) que demonstre como o re-ranking melhora a qualidade dos trechos recuperados para uma consulta de teste.

3.  **Métricas Básicas de Qualidade:**
    - Definição e medição de pelo menos uma métrica simples para avaliar a qualidade do RAG, como "Precisão da Fonte" (o sistema recuperou o documento correto?).

4.  **Diagrama de Arquitetura:**
    - Uma atualização no arquivo `docs/architecture.md` com um diagrama que ilustre o novo fluxo do RAG (Ingestão e Consulta).

## 🚀 Como Começar

1.  **Escolha seu Vector DB:** Decida se usará uma biblioteca local como ChromaDB (recomendado para começar) ou um serviço gerenciado.
2.  **Desenvolva o Pipeline de Ingestão:** Crie um script em `src/rag/ingestion.py` que leia os arquivos da `knowledge_base`, aplique uma estratégia de chunking e os insira no banco de dados vetorial.
3.  **Refatore o Serviço de Análise:** Modifique o serviço criado no Projeto 1. Agora, ele não chama o LLM diretamente. Ele primeiro chama um novo "serviço de recuperação" para obter o contexto.
4.  **Construa o Serviço de Recuperação:** Crie a lógica em `src/rag/retrieval.py` que, dada uma query, a converte em um embedding e consulta o banco de dados vetorial.
5.  **Implemente o Re-ranking:** Após a recuperação inicial, aplique uma técnica de re-ranking para otimizar a ordem dos resultados antes de enviá-los ao prompt.

---

Ao final deste projeto, nossa solução deixará de ser apenas uma "API inteligente" para se tornar um verdadeiro **sistema de conhecimento**, capaz de raciocinar com base em informações auditáveis e atualizáveis.