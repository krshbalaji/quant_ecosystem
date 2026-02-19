# core/strategy_container.py

active_strategies = {}
frozen_strategies = []

def register_strategy(name, obj):
    active_strategies[name] = obj

def freeze_all():
    global frozen_strategies
    frozen_strategies = list(active_strategies.keys())
    active_strategies.clear()

def get_active():
    return active_strategies

def get_frozen():
    return frozen_strategies
