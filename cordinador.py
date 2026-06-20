import requests
import json

# Datos para el disparo
token = "SU_TOKEN_AQUÍ"
page_id = "SU_PAGE_ID"
video_url = "URL_DEL_VIDEO"
descripcion = "Contenido de alta calidad"

url = f"https://graph.facebook.com/v23.0/{page_id}/videos"
headers = {"Authorization": f"Bearer {token}"}
payload = {"file_url": video_url, "description": descripcion}

# Ejecutar
respuesta = requests.post(url, headers=headers, data=payload)
print(json.dumps(respuesta.json(), indent=4))
