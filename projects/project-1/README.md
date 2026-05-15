# Projeto 1 – API Inteligente de Análise de Conformidade

**Objetivo:** Construir um **Serviço Especialista** em formato de API REST. Este serviço simula um analista de compliance, fornecendo uma análise automatizada de recomendações de investimento.

---

## 📝 Cenário de Negócio (FSO - Financial Services Office)

**A Dor:** Analistas de compliance gastam um tempo enorme revisando manualmente comunicações para garantir a adequação ao perfil de risco do cliente. O processo é lento, caro e sujeito a falhas.

**Nossa Solução (Fase 1):** Vamos construir o **"Compliance Checker API"**, um serviço que recebe uma recomendação de investimento e usa um LLM para fazer uma análise inicial, identificando potenciais violações. Este serviço será a principal ferramenta do nosso futuro agente autônomo.

## ⚙️ Configuração do Ambiente e Conexão com o LLM

Para que nossa API se comunique com o modelo de linguagem (LLM) de forma segura e robusta, vamos centralizar a lógica de conexão em um cliente reutilizável.

### 1. Crie o arquivo `.env`

Na raiz desta pasta (`projects/project-1/`), crie um arquivo chamado `.env`. Ele guardará suas credenciais de forma segura, seguindo o padrão da biblioteca `openai`.

```ini
# projects/project-1/.env
AZURE_OPENAI_ENDPOINT="seu-endpoint-aqui"
AZURE_OPENAI_KEY="sua-chave-aqui"
AZURE_OPENAI_API_VERSION="2024-06-01"
AZURE_DEPLOYMENT_NAME="seu-deployment-name-aqui"
```
**Importante:** Lembre-se de adicionar o arquivo `.env` ao seu `.gitignore` para nunca enviar suas credenciais para o repositório.

### 2. Acessando as Configurações no Código

Criamos uma classe `AzureModel` no arquivo `src/core/llm_client.py` que encapsula toda a lógica de conexão. Agora, em outros lugares do seu código, como nos seus serviços, você pode simplesmente importar e usar esta classe.

**Exemplo de implementação em `src/services/compliance_service.py`:**

```python
from ..core.llm_client import AzureModel
from ..api.schemas import AnalysisResult, AnalysisRequest # Exemplo de schemas

def analyze_recommendation(request: AnalysisRequest) -> AnalysisResult:
    """
    Usa o cliente LLM para analisar uma recomendação de investimento.
    """
    # 1. Instancia o cliente. As configurações são carregadas do .env automaticamente.
    llm_client = AzureModel()

    # 2. Cria um prompt estruturado para guiar o modelo.
    prompt = f"""
    Analise a seguinte recomendação de investimento: '{request.text}'.
    Verifique se ela é adequada para um cliente com perfil de risco '{request.client_profile}'.
    Retorne sua análise.
    """

    # 3. Invoca o modelo.
    try:
        response = llm_client.invoke(prompt=prompt)
        
        # Aqui você adicionaria a lógica para processar a resposta do LLM
        # e transformá-la no schema de resultado `AnalysisResult`.
        # Por exemplo, usando a biblioteca `instructor` para extração de dados.
        
        raw_content = response.choices[0].message.content
        
        # Exemplo simples de retorno (a ser refinado)
        return AnalysisResult(
            is_compliant= "não" not in raw_content.lower(),
            reason=raw_content,
            mentioned_products=[]
        )

    except Exception as e:
        print(f"Erro ao chamar o LLM: {e}")
        # Em um caso real, você retornaria uma resposta de erro HTTP.
        return AnalysisResult(
            is_compliant=False,
            reason=f"Falha ao processar a análise: {e}",
            mentioned_products=[]
        )
```

## 🚀 Como Começar: Guia Rápido

1.  **Setup do Ambiente:** Crie e ative um ambiente virtual Python na pasta `projects/project-1`.
    ```bash
    python -m venv .venv
    # Windows: .\.venv\Scripts\Activate.ps1 | macOS/Linux: source .venv/bin/activate
    ```

2.  **Instalar Dependências:** Crie um arquivo `requirements.txt` com as bibliotecas abaixo e execute `pip install -r requirements.txt`.
    ```
    fastapi
    uvicorn[standard]
    pydantic
    python-dotenv
    openai
    instructor
    ```

3.  **Desenvolver a API:** Siga a estrutura de pastas proposta, implementando a lógica no `main.py`, `services/` e `api/schemas.py`.

4.  **Testar:** Execute `uvicorn src.main:app --reload` e use a interface do Swagger UI em `http://127.0.0.1:8000/docs` para testar sua API.

## 🏛️ Estrutura do Projeto

Para manter nosso código organizado e escalável, seguimos uma estrutura de pastas clara:

```
.
├── .env                # Arquivo para suas credenciais (NÃO versionado)
├── .gitignore          # Arquivos e pastas ignorados pelo Git
├── Dockerfile          # Define a imagem Docker da nossa API
├── README.md           # Este guia que você está lendo
├── requirements.txt    # Dependências Python do projeto
├── data/               # Para dados de entrada/saída, se necessário
├── docs/               # Documentação do projeto (arquitetura, decisões)
├── knowledge_base/     # Base de conhecimento para o RAG (Projeto 2)
├── src/                # Onde todo o nosso código-fonte Python vive
│   ├── __init__.py
│   ├── main.py         # Ponto de entrada da API (FastAPI app)
│   ├── api/            # Módulos relacionados à API (endpoints, schemas)
│   ├── core/           # Configurações centrais e lógica de negócio principal
│   ├── services/       # Lógica de serviço (ex: chamar o LLM)
│   └── ...             # Outros módulos como `rag/`, `agents/`
└── tests/              # Testes automatizados
```

-   **`src/`**: O coração da aplicação. Todo o código Python vai aqui.
-   **`src/main.py`**: Define e configura a aplicação FastAPI. É o ponto de entrada que o `uvicorn` executa.
-   **`src/api/`**: Contém os endpoints da API e os `schemas` (modelos Pydantic) que definem os contratos de dados.
-   **`src/services/`**: Contém a lógica de negócio desacoplada da API. Por exemplo, a função que chama o LLM.
-   **`docs/`**: Para toda a documentação que não é o README. Ideal para diagramas de arquitetura e documentos de decisão.
-   **`tests/`**: Onde os testes unitários e de integração devem ser criados.

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
