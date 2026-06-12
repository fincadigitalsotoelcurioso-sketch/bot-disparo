import requests
import json
import os

# --- CONFIGURACIÓN DE GUERRA (Sustituya solo aquí) ---
TOKEN = "SU_TOKEN_EAAG_AQUI"
PAGE_ID = "SU_PAGE_ID_AQUI"
LINK_FINCA = "https://tu-link-aqui.com"


class FincaDigitalPro:
    def __init__(self):
        self.base_url = f"https://graph.facebook.com/v22.0/{PAGE_ID}/messages"
        self.headers = {"Content-Type": "application/json"}

    def procesar_mensaje(self, psid, texto):
        texto = texto.lower()
        if any(palabra in texto for palabra in ["info", "precio", "costo", "valor"]):
            return self.enviar_respuesta(
                psid,
                f"¡Soto el Curioso a sus órdenes! Vea aquí el link secreto: {LINK_FINCA}",
            )
        return None

    def enviar_respuesta(self, psid, respuesta):
        payload = {
            "recipient": {"id": psid},
            "message": {"text": respuesta},
            "access_token": TOKEN,
        }
        try:
            r = requests.post(
                self.base_url,
                params={"access_token": TOKEN},
                json={"recipient": {"id": psid}, "message": {"text": respuesta}},
            )
            return r.status_code == 200
        except Exception as e:
            print(f"Error crítico: {e}")
            return False


if __name__ == "__main__":
    bot = FincaDigitalPro()
    print("--- Bunker Soto el Curioso: ON LINE ---")
    # Aquí iría el loop de escucha (Webhook listener)
    # Por ahora, el motor está listo y blindado.
from flask import Flask, request, jsonify

app = Flask(__name__)


# Función que clasifica el mensaje (aquí está la lógica del bunker)
def clasificar_lead(mensaje):
    mensaje_lower = mensaje.lower()
    # Lógica de clasificación rápida
    if any(
        palabra in mensaje_lower
        for palabra in ["precio", "info", "informacion", "quiero"]
    ):
        return "INTERESADO"
    return "CURIOSEANDO"


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    # Facebook verifica el túnel con un GET
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == "MI_TOKEN_SECRETO":
            return challenge
        return "Error de verificación", 403

    # Aquí es donde caen los mensajes reales (POST)
    data = request.json
    try:
        mensaje = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        clasificacion = clasificar_lead(mensaje)
        print(f"--- NUEVO IMPACTO: '{mensaje}' | CLASIFICADO COMO: {clasificacion} ---")
    except:
        print("Recibido un paquete de Facebook, pero no es un mensaje de texto.")

    return jsonify({"status": "received"}), 200


if __name__ == "__main__":
    print("--- Bunker Soto el Curioso: ON LINE y esperando ---")
    app.run(port=5000)
