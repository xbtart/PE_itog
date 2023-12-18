# Итоговый проект - Веб-приложение для эмоционального анализа текста

Это веб-приложение использует FastAPI для создания REST API, которое позволяет анализировать эмоциональный тон текстов с использованием модели `cointegrated/rubert-tiny2-cedr-emotion-detection`. 

## Установка и запуск

1. Установите библиотеки, упомянутые в файле `requirements.txt`, используя следующую команду:

```bash
pip install -r requirements.txt
```

2. Запустите сервер с помощью команды:

```bash
uvicorn main:app --reload
```

## API endpoints

### POST /predict

Позволяет передать текст для анализа эмоционального тона.

#### Параметры запроса

- `text` (строка): Текст для анализа.

Пример запроса:
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"text": "Я очень удивлен происходящим!"}'
```

Пример успешного ответа:

```json
[
    [0.05, 0.78, 0.02, 0.08, 0.07]
]
```

Возвращается список вероятностей для каждой из пяти эмоций: ["грусть", "радость", "злость", "страх", "удивление"].

## Пример использования скрипта `send_request.py`

```python
import requests

text = "Я очень удивлен происходящим!"
url = "http://127.0.0.1:8000/predict?text="+text
payload = {"text": text}

response = requests.post(url, json=payload)
print(response.json())
```

## Требования

- fastapi==0.68.1
- torch==1.9.0
- transformers==4.10.2
- requests==2.26.0
- httpx==0.19.0
- pytest==7.0.1

## Запуск тестов

Чтобы запустить тесты, выполните команду:

```bash
pytest
```
