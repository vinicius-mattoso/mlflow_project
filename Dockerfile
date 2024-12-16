# Base Image
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos necessários
COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expondo a porta 5000
EXPOSE 5000

# Copiar o restante do projeto
COPY . .

# Comando padrão para execução
CMD ["bash"]
