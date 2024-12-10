import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def preprocess_data(input_path, output_dir):
    data = pd.read_csv(input_path)
    
    # Exemplo de pré-processamento
    X = data.drop(columns=["target"])
    y = data["target"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Dividir os dados
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # Salvar dados processados
    os.makedirs(output_dir, exist_ok=True)
    joblib.dump((X_train, X_test, y_train, y_test), os.path.join(output_dir, "processed_data.pkl"))
    joblib.dump(scaler, os.path.join(output_dir, "scaler.pkl"))
    print("Dados pré-processados e salvos em:", output_dir)
    
if __name__ == "__main__":
    preprocess_data("data/raw/dataset.csv", "data/processed")
