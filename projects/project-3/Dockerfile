# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de dependências
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY ./src .

# Exponha a porta que a aplicação vai usar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
