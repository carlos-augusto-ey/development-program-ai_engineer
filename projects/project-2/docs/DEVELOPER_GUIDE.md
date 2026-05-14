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

## 4. Versionamento e Padrão de Commits

Um histórico de versionamento limpo é uma forma de documentação e uma ferramenta de colaboração essencial. Adotaremos práticas padrão de mercado para garantir a clareza e a rastreabilidade do nosso trabalho.

### Fluxo de Trabalho com Branches (GitFlow Simplificado)

-   **`main`**: Esta branch é a nossa fonte da verdade. Ela deve conter apenas o código funcional e estável, representando as versões concluídas de cada projeto.
-   **`feature/<nome-da-feature>`**: Todo novo desenvolvimento, correção ou melhoria deve ser feito em uma branch separada, partindo da `main`.
    -   **Exemplos de Nomes:** `feature/cria-endpoint-analyze`, `fix/corrige-leitura-env`, `docs/atualiza-readme-projeto1`.
-   **Pull Requests (PRs):** Ao concluir o trabalho em uma `feature` branch, abra um Pull Request (ou Merge Request) para mesclar as alterações na `main`. Mesmo trabalhando sozinho, este processo simula um ambiente de *code review* e força uma revisão final antes da integração.

### Padrão de Mensagens de Commit (Conventional Commits)

Para manter o histórico legível e automatizável, siga o padrão [Conventional Commits](https://www.conventionalcommits.org/).

**Formato:** `<tipo>(<escopo>): <assunto>`

-   **Tipos Comuns:**
    -   `feat`: Uma nova funcionalidade (ex: `feat: adiciona endpoint de análise`).
    -   `fix`: Uma correção de bug (ex: `fix: trata erro de conexão com a API`).
    -   `docs`: Alterações na documentação (ex: `docs: atualiza o guia do desenvolvedor`).
    -   `style`: Mudanças que não afetam o significado do código (espaços, formatação).
    -   `refactor`: Uma mudança no código que não corrige um bug nem adiciona uma feature.
    -   `test`: Adicionando testes ou corrigindo testes existentes.
    -   `chore`: Mudanças em processos de build, ferramentas auxiliares, etc.

**Exemplo de uma boa mensagem de commit:**
`feat(api): implementa schema de resposta para o endpoint /analyze`