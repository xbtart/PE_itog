import requests

text = "Я очень удивлен происходящим!"
url = "http://127.0.0.1:8000/predict"

payload = {"text": text}
response = requests.post(url, json=payload)

print(response.json())