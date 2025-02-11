import os
import requests
import time
from dotenv import load_dotenv

# Cargar el token de Telegram desde .env
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def obtener_mensajes(offset=None):
    """Consulta los mensajes nuevos en Telegram usando polling."""
    params = {"offset": offset, "timeout": 30}
    response = requests.get(f"{TELEGRAM_API_URL}/getUpdates", params=params)
    return response.json()

def enviar_mensaje(chat_id, texto):
    """Envía un mensaje a Telegram."""
    requests.post(f"{TELEGRAM_API_URL}/sendMessage", json={"chat_id": chat_id, "text": texto})

def main():
    """Bucle principal para leer y responder mensajes."""
    print("🤖 Bot iniciado con polling...")
    offset = None
    while True:
        updates = obtener_mensajes(offset)
        if "result" in updates:
            for update in updates["result"]:
                chat_id = update["message"]["chat"]["id"]
                mensaje_texto = update["message"]["text"]
                
                # Responder al usuario
                respuesta = f"Recibí tu mensaje: {mensaje_texto}"
                enviar_mensaje(chat_id, respuesta)

                # Actualizar el offset para no recibir mensajes repetidos
                offset = update["update_id"] + 1

        time.sleep(2)  # Evita sobrecargar el servidor de Telegram

if __name__ == "__main__":
    main()

