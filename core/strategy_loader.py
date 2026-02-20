import os
import importlib.util
import inspect

STRATEGY_FOLDER = "strategies/active"


def load_strategies():
    strategies = []

    if not os.path.exists(STRATEGY_FOLDER):
        print("⚠ No active strategy folder found.")
        return strategies

    for file in os.listdir(STRATEGY_FOLDER):

        if not file.endswith(".py"):
            continue

        path = os.path.join(STRATEGY_FOLDER, file)

        try:
            spec = importlib.util.spec_from_file_location(file[:-3], path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if hasattr(obj, "generate_signal"):
                    strategies.append(obj())

        except Exception as e:
            print(f"⚠ Skipping {file} due to error: {e}")
            continue

    print(f"✅ Loaded {len(strategies)} active strategies.")
    return strategies