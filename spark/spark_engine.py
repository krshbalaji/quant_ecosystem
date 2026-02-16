"""
Spark Engine - Safe Coordinator
"""

import time
import os


class SparkEngine:

    def __init__(self):

        print("Spark Engine initialized")


    def scan(self):

        try:

            print("Spark: scanning strategy folder")

            strategies = os.listdir("strategies")

            count = len([s for s in strategies if s.endswith(".py")])

            print(f"Spark: {count} strategies available")

        except Exception as e:

            print("Spark error:", e)


    def run_loop(self):

        while True:

            self.scan()

            time.sleep(600)
