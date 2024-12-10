# Imagem base
FROM python:3.8-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY backend/requirements.txt /app/requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo da pasta backend para o contêiner
COPY backend/ /app/

# Defina o comando padrão para o contêiner
CMD ["python", "scripts/train_model.py"]
