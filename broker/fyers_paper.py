"""
PaperBroker
Simulates broker execution safely
Used for PAPER trading mode
"""

import datetime


class PaperBroker:

    def __init__(self):

        self.balance = 8000  # initial paper capital
        self.positions = {}

        print("PaperBroker initialized with balance:", self.balance)


    def get_available_funds(self):

        return self.balance


    def place_order(self, symbol, side, qty, price):

        value = qty * price

        if side == "BUY":

            if value > self.balance:

                print("PaperBroker: Insufficient funds")

                return None

            self.balance -= value

            self.positions[symbol] = {

                "qty": qty,
                "price": price,
                "side": side,
                "time": str(datetime.datetime.now())
            }

        elif side == "SELL":

            self.balance += value

            if symbol in self.positions:

                del self.positions[symbol]


        order = {

            "symbol": symbol,
            "side": side,
            "qty": qty,
            "price": price,
            "status": "FILLED",
            "timestamp": str(datetime.datetime.now())
        }

        print("PaperBroker Order:", order)

        return order


    def get_positions(self):

        return self.positions


    def get_balance(self):

        return self.balance
