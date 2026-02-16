import os
import requests
from dotenv import load_dotenv

from core.token_manager import TokenManager
from fyers_apiv3 import fyersModel

class FyersBroker:

    def __init__(self):

        tm = TokenManager()

        access_token = tm.get_access_token()

        self.fyers = fyersModel.FyersModel(
            client_id=tm.client_id,
            token=access_token,
            log_path=""
        )

        print("FYERS Broker Connected Securely")


        # Lazy load fyers model
        from fyers_apiv3 import fyersModel

        self.fyers = fyersModel.FyersModel(
            client_id=self.client_id,
            token=self.access_token,
            log_path=""
        )

    # -----------------------------------

    def get_quote(self, symbol):

        url = "https://api-t1.fyers.in/data/quotes"

        params = {
            "symbols": symbol
        }

        response = requests.get(
            url,
            headers=self.headers,
            params=params
        )

        if response.status_code != 200:
            raise Exception(
                f"HTTP Error {response.status_code}: {response.text}"
            )

        data = response.json()

        if data.get("s") != "ok":
            raise Exception(data)

        return data["d"][0]["v"]["lp"]

    # -----------------------------------

    def place_order(self, symbol, side, qty):

        url = "https://api-t1.fyers.in/api/v3/orders"

        payload = {
            "symbol": symbol,
            "qty": qty,
            "type": 2,
            "side": 1 if side == "BUY" else -1,
            "productType": "INTRADAY",
            "limitPrice": 0,
            "stopPrice": 0,
            "validity": "DAY",
            "disclosedQty": 0,
            "offlineOrder": False
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        return response.json()
