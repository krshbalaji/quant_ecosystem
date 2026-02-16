import os

MAX_STRATEGIES = 50


def enforce_limit():

    folder = "strategies"

    files = sorted(
        [f for f in os.listdir(folder) if f.startswith("strategy_")],
        key=lambda x: os.path.getctime(os.path.join(folder, x))
    )

    if len(files) > MAX_STRATEGIES:

        remove = files[:-MAX_STRATEGIES]

        for f in remove:

            os.remove(os.path.join(folder, f))

            print("Removed old strategy:", f)
