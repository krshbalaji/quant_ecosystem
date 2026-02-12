# =========================================
# OPTIONS EXECUTION ENGINE
# =========================================

from options.strike_selector import StrikeSelector
from options.option_symbol_builder import OptionBuilder


class OptionsEngine:

    def __init__(self, broker):
        self.broker = broker

    def execute(self, symbol, side, price, qty):

        strike = StrikeSelector.get_atm(price, symbol)

        opt_symbol = OptionBuilder.build(symbol, strike, side)

        self.broker.place_order(side, opt_symbol, qty, price)

        return opt_symbol
