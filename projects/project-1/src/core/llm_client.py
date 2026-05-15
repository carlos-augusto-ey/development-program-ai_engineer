import os
import logging
from typing import Optional

from dotenv import load_dotenv
import instructor
from openai import AzureOpenAI, ChatCompletion

# Carrega as variáveis de ambiente do arquivo .env da raiz do projeto 1
load_dotenv()

# Configuração do logger para este módulo
logger = logging.getLogger(__name__)


class AzureModel:
    """
    Um wrapper para o cliente Azure OpenAI que simplifica a inicialização
    e o uso de chamadas de completion, com suporte opcional para a biblioteca Instructor.
    """

    def __init__(
        self,
        temperature: float = 0.3,
        max_tokens: int = 4096,
        endpoint: Optional[str] = None,
        api_key: Optional[str] = None,
        deployment: Optional[str] = None,
        api_version: Optional[str] = None,
    ):
        """
        Inicializa o cliente. As configurações são lidas das variáveis de ambiente
        (AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, etc.) se não forem passadas diretamente.
        """
        self.endpoint = endpoint or os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_key = api_key or os.getenv("AZURE_OPENAI_KEY")
        self.deployment = deployment or os.getenv("AZURE_DEPLOYMENT_NAME")
        self.api_version = api_version or os.getenv("AZURE_OPENAI_API_VERSION")
        self.temperature = temperature
        self.max_tokens = max_tokens

        if not self.endpoint or not self.api_key or not self.deployment:
            logger.error("Configuração do Azure OpenAI incompleta.")
            raise ValueError(
                "As variáveis AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY e AZURE_DEPLOYMENT_NAME"
                " devem estar configuradas no arquivo .env."
            )

        logger.info("Inicializando cliente Azure OpenAI...")
        try:
            base_client = AzureOpenAI(
                azure_endpoint=self.endpoint,
                api_key=self.api_key,
                api_version=self.api_version,
            )
            # O cliente 'instructor' adiciona capacidades de extração de dados estruturados
            self.client = instructor.from_openai(base_client)
            self._base_client = base_client
            logger.info("Cliente Azure OpenAI inicializado com sucesso.")
        except Exception as e:
            logger.exception("Falha ao inicializar o cliente Azure OpenAI.")
            raise

    def invoke(self, prompt: str, max_tokens: Optional[int] = None) -> ChatCompletion:
        """
        Envia um único prompt para o modelo e retorna a resposta completa.

        Args:
            prompt: O texto a ser enviado para o modelo.
            max_tokens: O número máximo de tokens para a resposta (opcional).

        Returns:
            O objeto de resposta da API da OpenAI.
        """
        logger.info(f"Invocando modelo '{self.deployment}' com um prompt.")
        try:
            response = self._base_client.chat.completions.create(
                model=self.deployment,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=max_tokens or self.max_tokens,
            )
            logger.info("Resposta recebida do modelo.")
            return response

        except Exception as e:
            logger.exception(
                f"Erro durante a chamada para o modelo '{self.deployment}'."
            )
            raise
