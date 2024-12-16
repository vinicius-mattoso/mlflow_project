# MLflow Project - Versão 1

## Descrição
Este projeto demonstra como configurar e executar um servidor **MLflow** utilizando apenas um contêiner Docker. O MLflow será executado localmente e permitirá que você visualize experimentos e resultados na interface do MLflow UI.

---

## Estrutura do Projeto
A estrutura básica de arquivos para esta versão é a seguinte:

```
mlflow_project_v1/
│
├── Dockerfile         # Define o contêiner do MLflow server
├── data               # Store de dados
├── modelos            # Store de modelos
├── scripts            # Store de scripts
├── mlruns/            # Diretório para armazenar os experimentos do MLflow
└── README.md          # Documentação do projeto
```

- **Dockerfile**: Configura o contêiner Docker para rodar o MLflow UI.
- **data/**: Diretório para armazenamento de dados brutos.
- **modelos/**: Diretório onde os modelos treinados serão armazenados.
- **scripts/**: Diretório contendo os scripts Python para download, preprocessamento e treinamento.
- **mlruns/**: Diretório onde serão armazenados os logs e modelos gerados pelo MLflow.
- **README.md**: Documentação detalhada sobre como configurar e executar o projeto.

---

## Pré-requisitos
- Docker instalado ([Download e instalação](https://www.docker.com/get-started))
- Ou ambiente Python com bibliotecas do arquivo `requirements.txt` instaladas.

---

## Passos para Execução

1. **Construir a Imagem Docker**

   Execute o seguinte comando no terminal para construir a imagem Docker:

   ```bash
   docker build -t ml-project .
   ```

   - `-t ml-project`: Nome da imagem Docker a ser criada.
   - `.`: Indica que o Dockerfile está no diretório atual.

2. **Fazer o Download do Dataset**

   Utilize o script `download_data.py` dentro do contêiner para baixar os dados:

   ```bash
   docker run --rm -v $(pwd):/app ml-project python scripts/download_data.py
   ```

   - `-v $(pwd):/app`: Mapeia o diretório atual para o contêiner, permitindo que os dados sejam persistidos localmente.

3. **Pré-processar os Dados**

   Execute o script de preprocessamento dos dados:

   ```bash
   docker run --rm -v $(pwd):/app ml-project python scripts/data_preprocessing.py
   ```

4. **Treinar o Modelo**

   Treine o modelo utilizando o script `train_model.py`:

   ```bash
   docker run --rm -v $(pwd):/app ml-project python scripts/train_model.py
   ```

5. **Avaliar o Modelo**

   Avalie o modelo treinado com o script `evaluate_model.py`:

   ```bash
   docker run --rm -v $(pwd):/app ml-project python scripts/evaluate_model.py
   ```

6. **Visualizar os Resultados dos Experimentos**

   Para visualizar os resultados dos experimentos no MLflow UI, execute o comando abaixo para iniciar a interface localmente:

   ```bash
   mlflow ui
   ```

   Em seguida, acesse no navegador:

   ```
   http://localhost:5000
   ```

7. **Executar Todo o Processo de Forma Automática**

   Utilize o script `run_pipeline.ps1` para executar todo o pipeline de forma automatizada (somente em sistemas Windows):

   ```bash
   ./run_pipeline.ps1
   ```

---

## Resumo

- Este projeto cria um servidor MLflow simples usando Docker.
- Inclui scripts para download, preprocessamento, treinamento e avaliação.
- Os experimentos são armazenados em um diretório persistente chamado `mlruns`.
- O MLflow UI pode ser acessado via navegador em `http://localhost:5000`.

### Próximos Passos
- Expandir o projeto para incluir múltiplos contêineres com Docker Compose.
- Adicionar scripts mais avançados para registrar modelos e métricas no MLflow.
