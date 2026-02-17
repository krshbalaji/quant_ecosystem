import os
from dotenv import load_dotenv

load_dotenv()


# TELEGRAM
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")


# FYERS
FYERS_CLIENT_ID = os.getenv("FYERS_CLIENT_ID", "")
FYERS_ACCESS_TOKEN = os.getenv("FYERS_ACCESS_TOKEN", "")
FYERS_REFRESH_TOKEN = os.getenv("FYERS_REFRESH_TOKEN", "")
