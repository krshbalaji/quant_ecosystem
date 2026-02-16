import os
from fyers_apiv3 import fyersModel
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("FYERS_CLIENT_ID")
secret_key = os.getenv("FYERS_SECRET_KEY")
redirect_uri = os.getenv("FYERS_REDIRECT_URI")

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type="code",
    grant_type="authorization_code"
)

auth_url = session.generate_authcode()

print("\nOpen this URL in browser:\n")
print(auth_url)
