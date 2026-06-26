import requests

URL = "http://127.0.0.1:5000/api/protegido"
TOKEN = "segredo-da-turma-123"

# Cenário 1: Enviando o Token Correto no formato Bearer
cabecalhos = {"Authorization": f"Bearer {TOKEN}"}
print(">> Caso 1: Com token valido:")
r1 = requests.get(URL, headers=cabecalhos)
print("   Status:", r1.status_code, "| Resposta:", r1.json())

# Cenário 2: Tentando acessar sem passar o cabeçalho de autenticação
print("\n>> Caso 2: Sem token nenhum:")
r2 = requests.get(URL)
print("   Status:", r2.status_code, "| Resposta:", r2.json())

# Cenário 3: Forçando um token incorreto
print("\n>> Caso 3: Com token errado:")
r3 = requests.get(URL, headers={"Authorization": "Bearer chute-errado"})
print("   Status:", r3.status_code, "| Resposta:", r3.json())