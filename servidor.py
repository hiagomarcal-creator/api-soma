from flask import Flask, request, jsonify
2
3 app = Flask(__name__)
4
5 # Rota 1: GET http://127.0.0.1:5000/api/soma?a=2&b=3
6 @app.route("/api/soma", methods=["GET"])
7 def soma():
8 # Le os parametros ’a’ e ’b’ da URL (query string)
9 a = request.args.get("a", type=float)
10 b = request.args.get("b", type=float)
11
12 # Validacao simples (passo na direcao de "aplicacoes seguras")
13 if a is None or b is None:
14 return jsonify({"erro": "informe a e b, ex: ?a=2&b=3"}), 400
15
16 return jsonify({"resultado": a + b})
17
18 if __name__ == "__main__":
19 app.run(host="127.0.0.1", port=5000, debug=True)