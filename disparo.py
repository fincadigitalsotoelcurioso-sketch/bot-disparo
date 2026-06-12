from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


# Configuración básica del servidor
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Verificación con Meta
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == "MI_TOKEN_SECRETO":
            return challenge, 200
        return "Token incorrecto", 403

    if request.method == "POST":
        data = request.json
        print("Datos recibidos:", data)
        return jsonify({"status": "recibido"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
