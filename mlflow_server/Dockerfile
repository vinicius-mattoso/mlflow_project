# Dockerfile para o MLflow Server
FROM python:3.8-slim

# Instalar MLflow
RUN pip install mlflow

# Expor a porta do MLflow UI
EXPOSE 5000

# Rodar o MLflow UI
CMD ["mlflow", "ui", "--host", "0.0.0.0", "--backend-store-uri", "/mlruns"]
