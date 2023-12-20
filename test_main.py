# Разработчик #1 @aleksrf1 aleksrf@gmail.com - тест для api
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict():
    # Подготовка тестовых данных
    text = "Я очень удивлен происходящим!"

    # Выполнение запроса
    response = client.post("/predict?text=" + text, json={"text": text})

    # Проверка статуса ответа
    assert response.status_code == 200, "Not status code 200"

    predictions = response.json()

    # Проверка типа содержимого ответа
    assert response.headers["content-type"] == "application/json", "Not json application"
