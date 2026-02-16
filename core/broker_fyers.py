import os
from dotenv import load_dotenv

load_dotenv()

class FyersBroker:

    def __init__(self):

        self.client_id = os.getenv("FYERS_CLIENT_ID")
        self.access_token = os.getenv("FYERS_ACCESS_TOKEN")

        if not self.client_id or not self.access_token:
            raise Exception("FYERS credentials missing in .env")

        self.headers = {
            "Authorization": f"{self.client_id}:{self.access_token}",
            "Content-Type": "application/json"
        }

        print("FYERS Broker Connected Securely")
