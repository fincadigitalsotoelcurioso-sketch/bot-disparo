import requests
import json

# --- CONFIGURACIÓN (Ponga sus datos reales aquí) ---
TOKEN = "SU_TOKEN_AQUÍ"
PAGE_ID = "SU_PAGE_ID"
VIDEO_URL = "URL_DEL_VIDEO_AQUÍ"

url = f"https://graph.facebook.com/v23.0/{PAGE_ID}/videos"
headers = {"Authorization": f"Bearer {TOKEN}"}
# 11: Definición correcta (sin guiones)
payload = {
    "file_url": VIDEO_URL, 
    "description": "Disparo automático con bendición",
    "published": "true"
}

# 13 a 15: Conexión blindada
try:
    print("Iniciando conexión con Facebook...")
    # Aquí usamos 'data=payload', así es como Python entiende que debe enviar los datos
   respuesta = requests.post(url, headers=headers, data=payload)

    # Verificamos si la respuesta es exitosa (código 200)
    if respuesta.status_code == 200:
        print("¡ÉXITO! El servidor respondió correctamente:")
        print(json.dumps(respuesta.json(), indent=4))
    else:
        print(f"ERROR: Facebook respondió con código {respuesta.status_code}")
        print("Detalle del error:")
        print(respuesta.text)

except Exception as e:
    print(f"Ocurrió un error crítico al conectar: {e}")
