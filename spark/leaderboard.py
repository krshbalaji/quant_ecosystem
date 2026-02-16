import os
import json
from flask import jsonify

VAULT_FILE = "brain/spark_vault.json"


def leaderboard():
    print("DEBUG: Leaderboard called")

    if not os.path.exists(VAULT_FILE):
        return jsonify({"error": "vault file not found"}), 404

    with open(VAULT_FILE, "r") as f:
        data = json.load(f)

    print("DEBUG: Data loaded:", data)

    # Ensure list format
    if isinstance(data, dict):
        data = [data]

    leaderboard = {}

    for idea in data:

        if not isinstance(idea, dict):
            continue

        contributor = idea.get("author", "Unknown")

        stability = idea.get("stability_score", 0)
        impact = idea.get("impact_score", 0)
        success = idea.get("success_rating") or 0

        score = (stability * 0.4) + (impact * 0.4) + (success * 0.2)

        leaderboard[contributor] = leaderboard.get(contributor, 0) + score

    sorted_board = sorted(
        leaderboard.items(),
        key=lambda x: x[1],
        reverse=True
    )

    result = [
        {"contributor": name, "score": round(score, 2)}
        for name, score in sorted_board
    ]

    print("DEBUG: Leaderboard result:", result)

    return jsonify(result)
