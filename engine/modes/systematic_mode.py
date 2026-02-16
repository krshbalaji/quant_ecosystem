from .base_mode import BaseMode

class SystematicMode(BaseMode):

    def run(self):

        for strat in self.engine.strategy_selector.get_all():

            signal = strat.generate_signal()

            if signal:
                self.engine.execute_trade(signal)
