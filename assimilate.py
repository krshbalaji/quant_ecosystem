from core.assimilation_engine import AssimilationEngine

engine = AssimilationEngine()

content = input("Paste strategy, video link, or script:\n")

engine.assimilate(content)
