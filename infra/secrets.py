import os
from dotenv import load_dotenv

load_dotenv()


# TELEGRAM
# infra/secrets.py

TELEGRAM_TOKEN = "8568712333:AAEN-ANL0xSCcc5ck0j0ZsNww2rX_tyV4U8"
TELEGRAM_CHAT_ID = "7820843780"


# FYERS
FYERS_CLIENT_ID = os.getenv("FYERS_CLIENT_ID", "")
FYERS_ACCESS_TOKEN = os.getenv("FYERS_ACCESS_TOKEN", "")
FYERS_REFRESH_TOKEN = os.getenv("FYERS_REFRESH_TOKEN", "")
