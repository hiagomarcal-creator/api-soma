from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota 1: GET http://127.0.0.1:5000/api/soma?a=2&b=3
@app.route("/api/soma", methods=["GET"])
def soma():
    # Le os parametros 'a' e 'b' da URL (query string)
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    # Validacao simples (passo na direcao de "aplicacoes seguras")
    if a is None or b is None:
        return jsonify({"erro": "informe a e b, ex: ?a=2&b=3"}), 400

    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)