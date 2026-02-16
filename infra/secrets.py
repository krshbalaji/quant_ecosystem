import os
from dotenv import load_dotenv

load_dotenv()

def get_telegram_token():
    return os.getenv("TELEGRAM_TOKEN")

def get_telegram_chat_id():
    return os.getenv("TELEGRAM_CHAT_ID")
