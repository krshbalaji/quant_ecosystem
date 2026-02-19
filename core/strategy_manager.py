import os
import shutil

BASE_PATH = "strategies"

ACTIVE_PATH = os.path.join(BASE_PATH, "active")
FROZEN_PATH = os.path.join(BASE_PATH, "frozen")
ARCHIVED_PATH = os.path.join(BASE_PATH, "archived")
EXPERIMENTAL_PATH = os.path.join(BASE_PATH, "experimental")


def list_active():
    return [f for f in os.listdir(ACTIVE_PATH) if f.endswith(".py")]


def list_frozen():
    return [f for f in os.listdir(FROZEN_PATH) if f.endswith(".py")]


def list_experimental():
    return [f for f in os.listdir(EXPERIMENTAL_PATH) if f.endswith(".py")]


def activate_strategy(name):
    src = os.path.join(FROZEN_PATH, name)
    dst = os.path.join(ACTIVE_PATH, name)

    if os.path.exists(src):
        shutil.move(src, dst)
        return True
    return False


def freeze_strategy(name):
    src = os.path.join(ACTIVE_PATH, name)
    dst = os.path.join(FROZEN_PATH, name)

    if os.path.exists(src):
        shutil.move(src, dst)
        return True
    return False


def archive_strategy(name):
    src = os.path.join(ACTIVE_PATH, name)
    dst = os.path.join(ARCHIVED_PATH, name)

    if os.path.exists(src):
        shutil.move(src, dst)
        return True
    return False
