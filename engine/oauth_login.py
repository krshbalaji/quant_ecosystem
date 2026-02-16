import requests
import yaml
import webbrowser

SECRETS_FILE = "config/secrets.yaml"

class FyersOAuth:

    def __init__(self):
        with open(SECRETS_FILE) as f:
            self.secrets = yaml.safe_load(f)

        self.client_id = self.secrets["fyers"]["client_id"]
        self.redirect_uri = self.secrets["fyers"]["redirect_uri"]
        self.secret_key = self.secrets["fyers"]["secret_key"]

    def generate_login_url(self):
        url = f"https://api.fyers.in/api/v2/generate-authcode?client_id={self.client_id}&redirect_uri={self.redirect_uri}&response_type=code"
        webbrowser.open(url)
        print("🔐 Login opened in browser.")

    def exchange_code(self, auth_code):
        url = "https://api.fyers.in/api/v2/token"

        payload = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "client_id": self.client_id,
            "secret_key": self.secret_key,
            "redirect_uri": self.redirect_uri
        }

        res = requests.post(url, json=payload).json()

        if "access_token" in res:
            self.secrets["fyers"]["access_token"] = res["access_token"]
            self.secrets["fyers"]["refresh_token"] = res["refresh_token"]

            with open(SECRETS_FILE, "w") as f:
                yaml.dump(self.secrets, f)

            print("✅ Login Successful. Tokens saved.")
        else:
            print("❌ Login failed:", res)
