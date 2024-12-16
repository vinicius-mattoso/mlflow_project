# Steps to run this project


1) Build the docker:

docker build -t ml-project .

2) Fazer o Download do dataset:

docker run --rm -v /c/Users/vinicius/Documents/repositorios/mlflow_project:/app ml-project python scripts/download_data.py

3) Pré-processar os dados:

docker run --rm -v /c/Users/vinicius/Documents/repositorios/mlflow_project:/app ml-project python scripts/data_preprocessing.py


4) Treinar o modelo:

docker run --rm -v /c/Users/vinicius/Documents/repositorios/mlflow_project:/app ml-project python scripts/train_model.py


5) Avaliar o modelo:

docker run --rm -v /c/Users/vinicius/Documents/repositorios/mlflow_project:/app ml-project python scripts/evaluate_model.py


6) Visualizar o resultado dos experimentos:

mlflow ui

7) Executar de maneira automática todo o processo usando um power script:

./run_pipeline.ps1

