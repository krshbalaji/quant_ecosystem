from fyers_apiv3 import fyersModel
import os
from dotenv import load_dotenv
import urllib.parse as urlparse

load_dotenv()

CLIENT_ID = os.getenv("FYERS_CLIENT_ID")
SECRET_KEY = os.getenv("FYERS_SECRET_KEY")
REDIRECT_URI = "http://127.0.0.1:5000/"

print("\nSTEP 1: Open this URL in browser:\n")

session = fyersModel.SessionModel(
    client_id=CLIENT_ID,
    secret_key=SECRET_KEY,
    redirect_uri=REDIRECT_URI,
    response_type="code",
    grant_type="authorization_code"
)

print(session.generate_authcode())

print("\nSTEP 2: Paste FULL redirected URL here:\n")

redirected_url = input("Paste full URL: ")

parsed = urlparse.urlparse(redirected_url)
auth_code = urlparse.parse_qs(parsed.query)['auth_code'][0]

print("\nauth_code extracted OK")

session.set_token(auth_code)

response = session.generate_token()

if response.get("s") == "ok":
    print("\nACCESS TOKEN GENERATED SUCCESSFULLY\n")
    print("Access Token:\n")
    print(response["access_token"])

    print("\nRefresh Token:\n")
    print(response["refresh_token"])

    # Save automatically
    def save_access_token(new_token):

        env_file = ".env"

        lines = []

        if os.path.exists(env_file):
            with open(env_file, "r") as f:
                lines = f.readlines()

        # remove old token line
        lines = [line for line in lines if not line.startswith("FYERS_ACCESS_TOKEN=")]

        # add new token
        lines.append(f"FYERS_ACCESS_TOKEN={new_token}\n")

        with open(env_file, "w") as f:
            f.writelines(lines)

        print("Access token updated in .env")

else:
    print("\nFAILED:")
    print(response)
