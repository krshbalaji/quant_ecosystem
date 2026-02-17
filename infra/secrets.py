import os
from dotenv import load_dotenv

load_dotenv()


# TELEGRAM
# infra/secrets.py

TELEGRAM_TOKEN = "YOUR_NEW_TOKEN"
TELEGRAM_CHAT_ID = "7820843780"


# FYERS
FYERS_CLIENT_ID = os.getenv("FYERS_CLIENT_ID", "")
FYERS_ACCESS_TOKEN = os.getenv("FYERS_ACCESS_TOKEN", "")
FYERS_REFRESH_TOKEN = os.getenv("FYERS_REFRESH_TOKEN", "")
