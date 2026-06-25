import requests

URL = "http://127.0.0.1:5000/api/soma"

# Em GET, os parametros vao na "query string": ?a=2&b=3
parametros = {"a": 2, "b": 3}

resposta = requests.get(URL, params=parametros)

print("Status:", resposta.status_code) # 200 = OK
print("Cabecalhos:", dict(resposta.headers)) # metadados da resposta
print("Corpo (JSON):", resposta.json()) # {'resultado': 5.0}