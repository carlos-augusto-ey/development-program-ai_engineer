# Projeto 2 – RAG Confiável com Re-ranking

**Objetivo:** Evoluir a "Compliance Checker API" para um sistema robusto de RAG (Retrieval-Augmented Generation), garantindo que as análises de conformidade sejam baseadas em uma base de conhecimento auditável e de alta qualidade.

---

## 📝 Cenário de Negócio (FSO - Financial Services Office)

**A Dor (Evolução):** A API que construímos no Projeto 1 funciona, mas tem uma limitação crítica: suas regras de negócio estão "congeladas" dentro do prompt. Se uma política de investimento mudar, um desenvolvedor precisa reescrever e reimplantar o código. A análise não é facilmente auditável, pois não podemos apontar para a cláusula exata da política que foi usada.

**Nossa Solução (Fase 2):** Vamos transformar nossa API em um **"Policy-Grounded RAG"**. Antes de pedir ao LLM para analisar uma recomendação, nosso sistema irá primeiro buscar os trechos mais relevantes dos documentos de política e os fornecerá como contexto. Isso garante que a decisão seja sempre baseada na documentação oficial e atualizada.

## 📚 A Base de Conhecimento

Para que nosso sistema RAG se torne um especialista em compliance financeiro, ele será alimentado com documentos oficiais do mercado brasileiro. A pasta `knowledge_base/` deve conter os seguintes tipos de documentos (em formato PDF):

1.  **Códigos de Regulação da ANBIMA:**
    *   **Fonte:** Site oficial da ANBIMA.
    *   **Objetivo:** Contêm as regras e melhores práticas para a distribuição de produtos de investimento. São a principal fonte para o dia a dia do compliance.
    *   **Exemplo:** "Código de Distribuição de Produtos de Investimento".

2.  **Resoluções da CVM (Comissão de Valores Mobiliários):**
    *   **Fonte:** Site oficial da CVM.
    *   **Objetivo:** Fornecem o arcabouço legal para o mercado. A mais importante para nosso caso é a que trata de **Suitability** (adequação do produto ao perfil do investidor).
    *   **Exemplo:** "Resolução CVM 30".

3.  **Documento de Perfil de Risco (API):**
    *   **Fonte:** O documento `analise_de_perfil_do_investidor.txt` já presente na pasta.
    *   **Objetivo:** Define as categorias de perfil de risco (Conservador, Moderado, Arrojado) e quais tipos de ativos são adequados para cada um.

## 🛠️ Tecnologias e Conceitos Chave

-   **Backend:** Python 3.11+
-   **Bancos de Dados Vetoriais:** Ferramentas como ChromaDB, FAISS, ou serviços de nuvem para armazenar e consultar embeddings.
-   **Técnicas de IA:**
    -   **Ingestão e Indexação:** O processo de ler, dividir (`chunking`) e vetorizar os documentos da `knowledge_base`.
    -   **Chunking Semântico:** Estratégias para dividir os documentos de forma inteligente, preservando o significado.
    -   **Filtros de Recuperação:** Técnicas para refinar a busca no banco de dados vetorial.
    -   **Strict Grounding:** Forçar o LLM a basear sua resposta exclusivamente no contexto recuperado.
    -   **Técnicas de Re-ranking:** Algoritmos para reordenar os resultados da busca, trazendo os mais relevantes para o topo.

## ✅ Entregáveis

Para concluir este projeto, você deverá entregar:

1.  **Pipeline de Ingestão de Dados:**
    -   Um script Python (`src/rag/ingestion.py`) que seja executável e idempotente.
    -   Ele deve ler todos os PDFs da pasta `knowledge_base/`, aplicar uma estratégia de `chunking` (divisão de texto) e armazenar os `chunks` e seus respectivos `embeddings` em um banco de dados vetorial local (ex: ChromaDB).

2.  **API RAG Funcional:**
    -   A API do Projeto 1 deve ser refatorada. O endpoint `POST /analyze` agora deve orquestrar o fluxo RAG:
        1.  Receber a requisição com o texto da recomendação.
        2.  Converter a requisição em uma consulta para o sistema de recuperação.
        3.  Buscar os `chunks` mais relevantes da base de conhecimento vetorial.
        4.  (Opcional, mas recomendado) Aplicar um `re-ranker` para melhorar a ordem dos `chunks` recuperados.
        5.  Construir um prompt enriquecido, contendo as regras e o contexto recuperado.
        6.  Chamar o LLM com o prompt enriquecido.
    -   O schema de resposta (Pydantic) deve ser atualizado para incluir as fontes usadas na análise, como `source_document` e `source_chunk_id`.

3.  **Análise de Qualidade do Retrieval:**
    -   Um Jupyter Notebook (`notebooks/rag_evaluation.ipynb`) ou script de teste.
    -   Este notebook deve conter uma análise clara, comparando os resultados da busca **antes e depois** da aplicação de um `re-ranker` para pelo menos 3 consultas de teste diferentes.
    -   O objetivo é provar com exemplos que o re-ranking está trazendo os resultados mais relevantes para o topo.

4.  **Documentação da Arquitetura:**
    -   Um diagrama no arquivo `docs/architecture.md` ilustrando o fluxo completo do sistema RAG, desde a ingestão dos documentos até a resposta da API.

## 🚀 Como Começar

1.  **Escolha seu Vector DB:** Decida se usará uma biblioteca local como ChromaDB (recomendado para começar) ou um serviço gerenciado.
2.  **Desenvolva o Pipeline de Ingestão:** Crie o script em `src/rag/ingestion.py`. Pense em como você vai lidar com a limpeza dos dados dos PDFs.
3.  **Refatore o Serviço de Análise:** Modifique o serviço criado no Projeto 1. Agora, ele não chama o LLM diretamente. Ele primeiro chama um novo "serviço de recuperação" para obter o contexto.
4.  **Construa o Serviço de Recuperação:** Crie a lógica em `src/rag/retrieval.py` que, dada uma query, a converte em um embedding e consulta o banco de dados vetorial.
5.  **Implemente o Re-ranking:** Após a recuperação inicial, aplique uma técnica de re-ranking para otimizar a ordem dos resultados antes de enviá-los ao prompt.

---

Ao final deste projeto, nossa solução deixará de ser apenas uma "API inteligente" para se tornar um verdadeiro **sistema de conhecimento**, capaz de raciocinar com base em informações auditáveis e atualizáveis.