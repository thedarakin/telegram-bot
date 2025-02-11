from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Verificar que las variables se han cargado correctamente
print("TELEGRAM_BOT_TOKEN:", os.getenv("TELEGRAM_BOT_TOKEN"))
print("TOGETHER_AI_TOKEN:", os.getenv("TOGETHER_AI_TOKEN"))
