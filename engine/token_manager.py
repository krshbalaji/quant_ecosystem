import requests
import yaml
import os
from datetime import datetime

SECRETS_FILE = "config/secrets.yaml"

class TokenManager:

    def __init__(self):
        with open(SECRETS_FILE) as f:
            self.secrets = yaml.safe_load(f)

        self.client_id = self.secrets["fyers"]["client_id"]
        self.refresh_token = self.secrets["fyers"].get("refresh_token")

    def refresh_access_token(self):
        print("🔄 Refreshing Fyers access token...")

        url = "https://api.fyers.in/api/v2/token"

        payload = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id
        }

        response = requests.post(url, json=payload)
        data = response.json()

        if "access_token" in data:
            self.secrets["fyers"]["access_token"] = data["access_token"]

            with open(SECRETS_FILE, "w") as f:
                yaml.dump(self.secrets, f)

            print("✅ Access token refreshed successfully")
            return data["access_token"]

        else:
            print("❌ Token refresh failed:", data)
            return None
