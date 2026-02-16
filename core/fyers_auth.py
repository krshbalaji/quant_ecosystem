"""
FyersBroker
Live broker interface for FYERS
Handles live trading execution
"""

import os
from fyers_apiv3 import fyersModel
from dotenv import load_dotenv
from core.token_manager import TokenManager


class FyersBroker:

    def __init__(self):

        load_dotenv()

        self.client_id = os.getenv("FYERS_CLIENT_ID")

        if not self.client_id:

            raise Exception("FYERS_CLIENT_ID not found in .env")

        tm = TokenManager()

        access_token = tm.get_access_token()

        self.fyers = fyersModel.FyersModel(
            client_id=self.client_id,
            token=access_token,
            log_path=""
        )

        print("FYERS Broker Connected Securely")


    def get_available_funds(self):

        try:

            response = self.fyers.funds()

            return float(response["fund_limit"][0]["equityAmount"])

        except:

            return 0


    def place_order(self, symbol, side, qty, price):

        order = {

            "symbol": symbol,
            "qty": qty,
            "type": 2,
            "side": 1 if side == "BUY" else -1,
            "productType": "INTRADAY",
            "limitPrice": price,
            "stopPrice": 0,
            "validity": "DAY",
            "disclosedQty": 0,
            "offlineOrder": False

        }

        response = self.fyers.place_order(order)

        print("FYERS Order:", response)

        return response


    def get_positions(self):

        return self.fyers.positions()


    def get_balance(self):

        return self.get_available_funds()
