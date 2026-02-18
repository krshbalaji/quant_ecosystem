# core/system_launcher.py

from core.rd_engine import RDEngine
from core.meta_intelligence import meta_intelligence
from core.mode_controller import mode_controller

class SystemLauncher:

    def __init__(self):
        print("==================================================")
        print("🏛 Institutional Quant Ecosystem Booting...")
        print("==================================================")

        self.rd = RDEngine()

    def start(self):

        regime = meta_intelligence.predict_regime()

        if meta_intelligence.should_trade_live():
            print("LIVE trading permitted")
        else:
            print("LIVE trading blocked by guardian")

        print(f"Mode: {mode_controller.get_mode()}")

        self.rd.evolve()

        print("✅ Institutional Ecosystem ACTIVE")
