from fyers_apiv3 import fyersModel

client_id = "YOUR_APP_ID"
access_token = "YOUR_ACCESS_TOKEN"

fyers = fyersModel.FyersModel(
    client_id=client_id,
    token=access_token
)
