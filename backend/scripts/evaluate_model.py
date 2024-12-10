import joblib
from sklearn.metrics import mean_squared_error

def evaluate_model(processed_data_path, model_path):
    # Carregar dados e modelo
    X_train, X_test, y_train, y_test = joblib.load(processed_data_path)
    model = joblib.load(model_path)
    
    # Avaliar o modelo
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"MSE no conjunto de teste: {mse}")

if __name__ == "__main__":
    evaluate_model("data/processed/processed_data.pkl", "models/random_forest.pkl")
