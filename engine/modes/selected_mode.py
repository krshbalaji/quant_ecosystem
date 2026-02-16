from .base_mode import BaseMode

class SelectedMode(BaseMode):

    def run(self):
        # Only chosen strategy
        strat = self.engine.strategy_selector.get_selected()

        signal = strat.generate_signal()

        if signal:
            self.engine.execute_trade(signal)
