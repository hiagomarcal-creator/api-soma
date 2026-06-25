from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota 1: GET http://127.0.0.1:5000/api/soma?a=2&b=3
@app.route("/api/soma", methods=["GET"])
def soma_get():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    if a is None or b is None:
        return jsonify({"erro": "informe a e b, ex: ?a=2&b=3"}), 400

    return jsonify({"resultado": a + b, "metodo": "GET"})

# Rota 2: POST http://127.0.0.1:5000/api/soma (Dados no corpo em JSON)
@app.route("/api/soma", methods=["POST"])
def soma_post():
    # Obtem os dados enviados no corpo da requisicao (JSON)
    dados = request.get_json()

    # Se nao enviar JSON ou faltar campos
    if not dados or "a" not in dados or "b" not in dados:
        return jsonify({"erro": "Envie um JSON no formato {'a': 2, 'b': 3}"}), 400

    a = float(dados["a"])
    b = float(dados["b"])

    return jsonify({"resultado": a + b, "metodo": "POST"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)