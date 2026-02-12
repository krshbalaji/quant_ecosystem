import schedule
import time


def start(job):

    schedule.every().day.at("09:05").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
