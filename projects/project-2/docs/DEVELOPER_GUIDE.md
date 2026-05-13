# Guia do Desenvolvedor - Projeto Compliance Checker

Este documento fornece diretrizes e padrões para o desenvolvimento do projeto, garantindo consistência e qualidade do código.

## 1. Padrões de Código

### Schemas Pydantic
- **Onde:** `src/api/schemas/`
- **Propósito:** Definir contratos de dados claros para as requisições e respostas da API.
- **Exemplo:**

```python
# src/api/schemas/analysis.py
from pydantic import BaseModel, Field
from typing import List

class AnalysisRequest(BaseModel):
    text_to_analyze: str = Field(..., min_length=10, description="Texto da recomendação a ser analisada.")

class AnalysisResponse(BaseModel):
    is_compliant: bool = Field(..., description="Indica se a recomendação está em conformidade.")
    reason: str = Field(..., description="Justificativa detalhada da análise.")
    mentioned_products: List[str] = Field([], description="Lista de produtos de investimento mencionados.")
```

### Lógica de Serviço
- **Onde:** `src/services/`
- **Propósito:** Isolar a lógica de negócio da camada de API. Funções aqui não devem ter conhecimento direto de `request` e `response` do FastAPI.
- **Exemplo:** A função `analyze_text` em `src/services/compliance_service.py` é um exemplo perfeito. Ela recebe dados brutos (uma string) e retorna um resultado (um dicionário ou um objeto de dados), sem se preocupar com o protocolo HTTP.

## 2. Gerenciamento de Erros

Para mantermos a API robusta e previsível, devemos adotar um padrão para tratamento de exceções.

- **Exceções de Negócio:** Crie exceções customizadas em `src/core/exceptions.py` para representar erros de negócio (ex: `ProdutoNaoEncontradoError`).
- **Tratamento na API:** Use um `try...except` nos endpoints da API para capturar essas exceções e retornar respostas HTTP apropriadas (ex: status 404 Not Found).

```python
# Exemplo em um endpoint
from fastapi import APIRouter, HTTPException
from src.services import compliance_service
from src.core.exceptions import APIConnectionError

router = APIRouter()

@router.post("/analyze")
async def analyze_recommendation(request: AnalysisRequest):
    try:
        result = compliance_service.analyze_text(request.text_to_analyze)
        if not result:
            raise APIConnectionError("Falha ao conectar com o serviço de análise.")
        return result
    except APIConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        # Erro genérico para casos não esperados
        raise HTTPException(status_code=500, detail="Ocorreu um erro interno no servidor.")

```

## 3. Testes

A qualidade do nosso projeto depende de uma boa cobertura de testes.

- **Onde:** `tests/`
- **Ferramenta:** `pytest`

### Testes Unitários
- **Foco:** Testar uma única função ou método de forma isolada.
- **Exemplo (`tests/test_services.py`):**
  - Testar a função `analyze_text` usando `mocks` (com `unittest.mock`) para simular a resposta da API do LLM, sem fazer uma chamada de rede real. Isso garante que o teste seja rápido e não dependa de um serviço externo.

### Testes de Integração
- **Foco:** Testar a interação entre diferentes partes do sistema.
- **Exemplo (`tests/test_api.py`):**
  - Usar o `TestClient` do FastAPI para fazer chamadas HTTP reais ao seu endpoint `/analyze`.
  - Verificar se a API retorna o status code correto (200, 422, 500, etc.) e se o corpo da resposta está no formato esperado (validado pelo schema Pydantic).
