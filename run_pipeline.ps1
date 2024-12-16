# Diretório do projeto no Windows
$dockerPath = "/c/Users/vinicius/Documents/repositorios/mlflow_project"

# Executar o pipeline
docker run --rm -v ${dockerPath}:/app ml-project python scripts/data_preprocessing.py
docker run --rm -v ${dockerPath}:/app ml-project python scripts/train_model.py
docker run --rm -v ${dockerPath}:/app ml-project python scripts/evaluate_model.py

