import requests
import json


def publicar_video_meta(access_token, page_id, video_url, descripcion):
    # La URL correcta para páginas (cambie 'me' por su page_id)
    url = f"https://graph.facebook.com/v23.0/{page_id}/videos"

    headers = {"Authorization": f"Bearer {access_token}"}

    # Estos son los parámetros que la API exige sí o sí
    payload = {"file_url": video_url, "description": descripcion}

    try:
        response = requests.post(url, headers=headers, data=payload)
        # Si esto da error, aquí veremos exactamente por qué
        return response.json()
    except Exception as e:
        return {"error": str(e)}


# Datos de combate
TOKEN = "PEGUE_AQUÍ_SU_TOKEN_SIN_LA_PALABRA_BEARER"
PAGE_ID = "EL_ID_DE_SU_PÁGINA"
VIDEO_URL = "URL_PÚBLICA_DEL_VIDEO"
DESCRIPCION = "Tamales hechos con determinación"

resultado = publicar_video_meta(TOKEN, PAGE_ID, VIDEO_URL, DESCRIPCION)
print(json.dumps(resultado, indent=4))
