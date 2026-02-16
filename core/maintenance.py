import subprocess
import datetime


def run_daily():

    print("Running daily maintenance...")

    subprocess.run(["git", "pull"])

    subprocess.run(["git", "add", "."])

    subprocess.run(["git", "commit", "-m", "auto maintenance"])

    subprocess.run(["git", "push"])


def should_run():

    now = datetime.datetime.now()

    return now.hour == 7 and now.minute >= 30 and now.minute <= 45
