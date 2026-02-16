import json
import datetime
import os

BACKLOG_PATH = "brain/spark_backlog.json"

class SparkEngine:

    def __init__(self):
        if not os.path.exists(BACKLOG_PATH):
            with open(BACKLOG_PATH, "w") as f:
                json.dump([], f)

    def load(self):
        with open(BACKLOG_PATH, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(BACKLOG_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def add_spark(self, title, category, impact, complexity, stability):
        data = self.load()

        priority = round((impact * stability) / max(complexity,1), 2)

        spark = {
            "id": len(data) + 1,
            "date": str(datetime.date.today()),
            "title": title,
            "category": category,
            "impact_score": impact,
            "complexity_score": complexity,
            "stability_weight": stability,
            "priority_score": priority,
            "status": "pending"
        }

        data.append(spark)
        self.save(data)

        print(f"✅ Spark Added | Priority Score: {priority}")

    def list_sparks(self):
        data = sorted(self.load(), key=lambda x: x["priority_score"], reverse=True)
        for s in data:
            print(s["id"], s["title"], "| Priority:", s["priority_score"], "|", s["status"])

    def approve(self, spark_id):
        data = self.load()
        for s in data:
            if s["id"] == spark_id:
                s["status"] = "approved"
        self.save(data)
        print("🚀 Spark Approved")

    def archive(self, spark_id):
        data = self.load()
        for s in data:
            if s["id"] == spark_id:
                s["status"] = "archived"
        self.save(data)
        print("📦 Spark Archived")
