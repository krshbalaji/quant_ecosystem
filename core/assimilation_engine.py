import re
import os
from datetime import datetime

class AssimilationEngine:

    def __init__(self, strategy_dir="strategies"):
        self.strategy_dir = strategy_dir
        os.makedirs(strategy_dir, exist_ok=True)

    def assimilate(self, content):

        logic = self.extract_logic(content)

        strategy_code = self.generate_strategy(logic)

        filename = f"strategy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"

        path = os.path.join(self.strategy_dir, filename)

        with open(path, "w") as f:
            f.write(strategy_code)

        print(f"New strategy assimilated: {filename}")

        return path

    def extract_logic(self, content):

        logic = {}

        if "RSI" in content.upper():
            logic["indicator"] = "RSI"

        if "MACD" in content.upper():
            logic["indicator2"] = "MACD"

        if "BUY" in content.upper():
            logic["buy"] = True

        if "SELL" in content.upper():
            logic["sell"] = True

        return logic

    def generate_strategy(self, logic):

        return f'''
import pandas as pd
import talib

class AssimilatedStrategy:

    name = "AssimilatedStrategy"

    def generate_signal(self, data):

        close = data["close"]

        rsi = talib.RSI(close)

        if rsi.iloc[-1] < 30:
            return "BUY"

        elif rsi.iloc[-1] > 70:
            return "SELL"

        return None
'''
