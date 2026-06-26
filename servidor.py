from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Em producao, isto viria de variavel de ambiente, NUNCA no codigo!
TOKEN_VALIDO = "segredo-da-turma-123"

# O "porteiro" da nossa API (Decorador de autenticacao)
def requer_token(funcao):
    @wraps(funcao)
    def envoltorio(*args, **kwargs):
        cabecalho = request.headers.get("Authorization", "")

        # 1) Precisa comecar com "Bearer "
        if not cabecalho.startswith("Bearer "):
            return jsonify({"erro": "token ausente"}), 401

        # 2) Extrai apenas a chave após a palavra "Bearer "
        try:
            token = cabecalho.split(" ", 1)[1]
        except IndexError:
            return jsonify({"erro": "formato de token invalido"}), 401

        # 3) Confere se o token enviado é o correto
        if token != TOKEN_VALIDO:
            return jsonify({"erro": "token invalido"}), 401

        return funcao(*args, **kwargs)
    return envoltorio

# Rota 1: GET
@app.route("/api/soma", methods=["GET"])
def soma_get():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a is None or b is None:
        return jsonify({"erro": "informe a e b, ex: ?a=2&b=3"}), 400
    return jsonify({"resultado": a + b, "metodo": "GET"})

# Rota 2: POST
@app.route("/api/soma", methods=["POST"])
def soma_post():
    dados = request.get_json(silent=True) or {}
    a = dados.get("a")
    b = dados.get("b")
    if a is None or b is None:
        return jsonify({"erro": "envie a e b no corpo JSON"}), 400
    return jsonify({"resultado": a + b, "metodo": "POST"})

# Rota 3: PROTEGIDA (Nova do Horário 4)
@app.route("/api/protegido", methods=["GET"])
@requer_token
def protegido():
    return jsonify({"mensagem": "Acesso autorizado! Dados secretos de Ciberseguranca aqui."})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)