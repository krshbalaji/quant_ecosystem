from .base_mode import BaseMode

class SwingMode(BaseMode):

    def run(self):

        signals = []

        for strat in self.engine.strategy_selector.get_all():
            s = strat.generate_signal()
            if s:
                signals.append(s)

        self.engine.telegram.notify(
            f"📊 Swing Signals:\n{signals}"
        )
