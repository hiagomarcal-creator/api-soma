import requests

URL = "http://127.0.0.1:5000/api/soma"

# Em POST, os dados vao escondidos no corpo (body) da requisicao
dados_corpo = {"a": 10, "b": 20}

# Mudamos para requests.post e usamos json= para enviar os dados
resposta = requests.post(URL, json=dados_corpo)

print("Status:", resposta.status_code)
print("Corpo (JSON):", resposta.json())