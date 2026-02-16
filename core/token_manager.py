import os
import json
from datetime import datetime, timedelta
from fyers_apiv3 import fyersModel
from dotenv import load_dotenv

class TokenManager:

    def __init__(self):

        load_dotenv()

        self.client_id = os.getenv("FYERS_CLIENT_ID")
        self.secret_key = os.getenv("FYERS_SECRET_KEY")
        self.redirect_uri = "http://127.0.0.1:5000/"

        self.token_file = "data/token.json"

        os.makedirs("data", exist_ok=True)


    def get_access_token(self):

        token_data = self._load_token()

        if token_data and not self._is_expired(token_data):
            return token_data["access_token"]

        print("Refreshing FYERS access token...")

        new_token = self._refresh(token_data["refresh_token"])

        self._save_token(new_token)

        return new_token["access_token"]


    def _refresh(self, refresh_token):

        session = fyersModel.SessionModel(
            client_id=self.client_id,
            secret_key=self.secret_key,
            grant_type="refresh_token"
        )

        session.set_token(refresh_token)

        response = session.generate_token()

        if response.get("s") != "ok":
            raise Exception("Token refresh failed. Run generate_token.py manually once.")

        return response


    def _is_expired(self, token):

        expiry = datetime.fromtimestamp(token["expiry"])

        return datetime.now() >= expiry - timedelta(minutes=5)


    def _load_token(self):

        if not os.path.exists(self.token_file):
            return None

        with open(self.token_file, "r") as f:
            return json.load(f)


    def _save_token(self, token):

        expiry = datetime.now() + timedelta(hours=12)

        data = {
            "access_token": token["access_token"],
            "refresh_token": token["refresh_token"],
            "expiry": expiry.timestamp()
        }

        with open(self.token_file, "w") as f:
            json.dump(data, f, indent=4)

        print("Token saved.")
