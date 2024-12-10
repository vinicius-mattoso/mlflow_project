import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

def train_model(processed_data_path, model_dir):
    # Carregar dados
    X_train, X_test, y_train, y_test = joblib.load(processed_data_path)

    # Configurar MLFlow
    mlflow.set_experiment("docker-ml-project")
    
    with mlflow.start_run():
        # Hiperparâmetros
        params = {"n_estimators": 100, "max_depth": 10, "random_state": 42}
        
        # Treinar modelo
        model = RandomForestRegressor(**params)
        model.fit(X_train, y_train)
        
        # Avaliar modelo
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        
        # Registrar no MLFlow
        mlflow.log_params(params)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")
        
        # Salvar modelo localmente
        os.makedirs(model_dir, exist_ok=True)
        joblib.dump(model, os.path.join(model_dir, "random_forest.pkl"))
        print("Modelo salvo em:", model_dir)
        
if __name__ == "__main__":
    train_model("data/processed/processed_data.pkl", "models")
