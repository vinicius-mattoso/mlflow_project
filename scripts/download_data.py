import os
import pandas as pd
from sklearn.datasets import fetch_california_housing

def download_and_save_data(output_dir):
    # Baixar o dataset
    print("Baixando o dataset California Housing Prices...")
    housing = fetch_california_housing(as_frame=True)
    
    # Criar DataFrame
    data = housing.frame
    data['target'] = housing.target  # Adicionar a variável-alvo
    
    # Criar diretório para salvar os dados
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "dataset.csv")
    
    # Salvar como CSV
    data.to_csv(output_file, index=False)
    print(f"Dataset salvo em: {output_file}")

if __name__ == "__main__":
    download_and_save_data("data/raw")
