# strategies container

import os
import json

STRATEGY_FOLDER = os.path.join(os.path.dirname(__file__), "active")
REGISTRY_FILE = os.path.join(os.path.dirname(__file__), "registry.json")

def get_active_strategies():
    if not os.path.exists(STRATEGY_FOLDER):
        return []

    return [
        f for f in os.listdir(STRATEGY_FOLDER)
        if f.endswith(".py")
    ]

def get_registry():
    if not os.path.exists(REGISTRY_FILE):
        return {}

    with open(REGISTRY_FILE, "r") as f:
        return json.load(f)


import importlib

def load_strategies():
    strategies = {}
    path = os.path.join(os.path.dirname(__file__), "active")

    for file in os.listdir(path):
        if file.endswith(".py") and file != "__init__.py":
            module_name = f"strategies.active.{file[:-3]}"
            module = importlib.import_module(module_name)

            if hasattr(module, "Strategy"):
                strategies[file[:-3]] = module.Strategy()

    return strategies
