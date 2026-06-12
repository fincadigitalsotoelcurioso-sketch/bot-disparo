import os
import shutil
import time

# CONFIGURACIÓN DEL EMBUDO (Parametrización)
CARPETA_BASE = r"C:\Users\WINDOWS\Downloads"
DIAS_PARA_LIMPIEZA = 7

# Definimos el destino según la naturaleza del flujo
EMBUDO_DESTINOS = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Media": [".mp4", ".jpg", ".png", ".mp3"],
    "Instaladores": [".exe", ".msi", ".apk", ".zip"],
}


def ejecutar_embudo():
    print("--- Iniciando parametrización del embudo de entrada ---")

    # Crear carpetas si no existen (Garantía de funcionamiento)
    for categoria in EMBUDO_DESTINOS:
        ruta_cat = os.path.join(r"C:\Users\WINDOWS\Documents", categoria)
        if not os.path.exists(ruta_cat):
            os.makedirs(ruta_cat)

    for nombre in os.listdir(CARPETA_BASE):
        ruta_origen = os.path.join(CARPETA_BASE, nombre)

        if os.path.isfile(ruta_origen):
            ext = os.path.splitext(nombre)[1].lower()
            movido = False

            # Lógica de clasificación (Embudo)
            for categoria, extensiones in EMBUDO_DESTINOS.items():
                if ext in extensiones:
                    shutil.move(
                        ruta_origen,
                        os.path.join(r"C:\Users\WINDOWS\Documents", categoria, nombre),
                    )
                    print(f"[CLASIFICADO] -> {categoria}: {nombre}")
                    movido = True
                    break

            # Lógica de limpieza (Si no se clasificó y es viejo)
            if not movido:
                if (time.time() - os.path.getmtime(ruta_origen)) / (
                    24 * 3600
                ) > DIAS_PARA_LIMPIEZA:
                    os.remove(ruta_origen)
                    print(f"[ELIMINADO] -> {nombre}")

    print("--- Embudo parametrizado: Tarea completada con éxito ---")


if __name__ == "__main__":
    ejecutar_embudo()
