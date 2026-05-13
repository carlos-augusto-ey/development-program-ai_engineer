# Projeto 1 – API Inteligente de Análise de Conformidade

**Objetivo:** Construir uma API REST baseada em LLM, com contratos bem definidos e pronta para execução em ambientes corporativos, que sirva como o primeiro nível de automação para análise de conformidade de investimentos.

---

## 📝 Cenário de Negócio (FSO - Financial Services Office)

**A Dor:** Em instituições financeiras, analistas de compliance gastam um tempo enorme revisando manualmente comunicações (e-mails, minutas) para garantir que as recomendações de investimento estejam alinhadas com as políticas de risco da empresa e o perfil de cada cliente. Esse processo é lento, caro e sujeito a falhas humanas.

**Nossa Solução (Fase 1):** Vamos construir o **"Compliance Checker API"**, um serviço que recebe o texto de uma recomendação de investimento e, usando um LLM, faz uma primeira análise automatizada, identificando potenciais violações de conformidade.

## 🛠️ Tecnologias e Conceitos Chave

- **Backend:** Python 3.11+
- **Framework da API:** FastAPI
- **Validação de Dados:** Pydantic
- **Containerização:** Docker
- **Técnicas de IA:**
  - Prompt Engineering Orientado a Produto
  - Tool-calling para Saídas Estruturadas (JSON)
  - Strict Grounding (em um nível básico)

## ✅ Entregáveis

Para concluir este projeto, você deverá entregar:

1.  **API Funcional e Documentada:**
    - Um endpoint `POST /analyze` que recebe um texto.
    - A API deve retornar uma resposta JSON estruturada, validada com Pydantic, contendo no mínimo:
      - `is_compliant` (boolean)
      - `reason` (string)
      - `mentioned_products` (list)
    - A documentação da API deve ser gerada automaticamente pelo FastAPI (via OpenAPI/Swagger).

2.  **Dockerfile:**
    - Um `Dockerfile` funcional que empacota a aplicação FastAPI, instala as dependências e a executa.

3.  **Contratos Versionados:**
    - Os schemas Pydantic que definem os contratos de request e response da sua API devem estar claramente definidos no diretório `src/api/schemas/`.

4.  **Documento de Decisões Técnicas:**
    - Um breve resumo no arquivo `docs/decisions.md` explicando as principais escolhas de design. Por exemplo: "Por que usamos Pydantic para forçar a saída do LLM?"

## 🚀 Como Começar

1.  **Setup do Ambiente:** Crie e ative um ambiente virtual Python.
2.  **Instalar Dependências:** Instale `fastapi`, `uvicorn`, e a biblioteca do seu LLM de preferência (ex: `openai`).
3.  **Estrutura do Código:** Comece a desenvolver sua lógica no arquivo `src/main.py` e organize os schemas em `src/api/schemas/`.
4.  **Desenvolver a API:** Crie o endpoint `/analyze` e a lógica de serviço que interage com o LLM.
5.  **Testar:** Use a interface do Swagger UI (`/docs`) para testar sua API interativamente.
6.  **Dockerizar:** Escreva e teste seu `Dockerfile`.

---

Este projeto é a fundação para os próximos. Uma API bem projetada aqui tornará a integração com o pipeline RAG (Projeto 2) e com o Agente (Projeto 3) muito mais simples.
