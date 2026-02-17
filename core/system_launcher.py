import threading
import time
import os
import shutil

from core.meta_controller import MetaController
from core.rd_engine import RDEngine
from core.federated_engine import FederatedEngine
from core.central_brain import CentralBrain
from core.system_guard import SystemGuard
from spark.spark_engine import SparkEngine
from spark.leaderboard import Leaderboard
from core.telegram_listener import listen
from dashboard import app as dashboard_app
from core.auto_deploy import AutoDeploy
from core.self_healing import SelfHealingEngine
from core.genetic_engine import GeneticEngine
from core.population_manager import PopulationManager


class SystemLauncher:

    def __init__(self, broker):

        self.broker = broker

        self.guard = SystemGuard()

        self.meta = MetaController(broker)

        self.rd = RDEngine()

        self.spark = SparkEngine()

        self.leaderboard = Leaderboard()

        self.federated = FederatedEngine()

        self.brain = CentralBrain()

        self.running = True

        self.deploy = AutoDeploy()

        self.healer = SelfHealingEngine()

        self.genetic = GeneticEngine()

        self.population = PopulationManager()

    def start(self):

        print("Starting Autonomous Ecosystem...")

        # download global brain
        self.brain.download()

        # start dashboard
        threading.Thread(
            target=self.run_dashboard,
            daemon=True
        ).start()

        # start telegram listener
        threading.Thread(
            target=listen,
            args=(self.broker,),
            daemon=True
        ).start()

        # start watchdog
        threading.Thread(
            target=self.run_watchdog,
            daemon=True
        ).start()

        # start core loop
        self.run_core_loop()

        self.deploy.sync()


    def run_dashboard(self):

        try:

            dashboard_app.run(
                host="0.0.0.0",
                port=5000,
                debug=False,
                use_reloader=False
            )

        except Exception as e:

            print("Dashboard error:", e)


    def run_core_loop(self):

        while self.running:

            try:

                decision = self.meta.decide()

                if decision["action"] == "TRADE":

                    print("Trading mode active")

                elif decision["action"] == "EVOLVE":

                    self.rd.run()

                self.spark.scan()

                self.leaderboard.update()

            except Exception as e:

                print("Core loop error:", e)

            time.sleep(300)


    def run_watchdog(self):

        while True:

            try:

                # system health check
                if not self.guard.alive():

                    print("SystemGuard detected issue")

                # federated sync
                self.federated.sync()

                # upload brain
                self.brain.upload()

                # aggregate brain
                self.brain.aggregate()

                # encrypted backup
                self.cloud_backup()

                self.deploy.upload()

                self.healer.heal()

                self.population.run()

            except Exception as e:

                print("Watchdog error:", e)

            time.sleep(300)


    def cloud_backup(self):

        try:

            src = "data/global_brain.pt"

            dst = "data/global_brain_backup.pt"

            if os.path.exists(src):

                shutil.copy(src, dst)

                print("Cloud backup updated")

        except Exception as e:

            print("Backup error:", e)
