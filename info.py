import re
from os import environ, getenv

API_ID = environ.get("API_ID", "29171167")
API_HASH = environ.get("API_HASH", "7ea2149629e445936619f06a3c0dc716")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER_ID = int(environ.get("OWNER_ID", "7251898668"))
DATABASE_URL = environ.get("DATABASE_URL",  "mongodb+srv://ai:ai@cluster0.fgu4b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002338054057"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "akmovieshubbackup"))
FSUB = environ.get("FSUB", True)
GOOGLE_API_KEY = environ.get('API_KEY', '')

PROMPT = """You are a helpful Python programmed AI chatbot on Telegram named "AI Neura Bot" created by "AKMOVIEBOTZ" He is known as @Akmovieshubbackup on Telegram. Also, you are a text improver and a perfect friend chatbot, and all your replies are in Hinglish."""
