import os
from fyers_apiv3 import fyersModel
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("FYERS_CLIENT_ID")
secret_key = os.getenv("FYERS_SECRET_KEY")
redirect_uri = os.getenv("FYERS_REDIRECT_URI")

auth_code = input("Enter auth_code: ")

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type="code",
    grant_type="authorization_code"
)

session.set_token(auth_code)

response = session.generate_token()

print("\nACCESS TOKEN:\n")
print(response["access_token"])
