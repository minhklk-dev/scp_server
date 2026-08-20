from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "database.json"

# Create file if missing
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"players": 0}, f)

@app.route("/played", methods=["POST"])
def played():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    data["players"] += 1
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    return jsonify(data)

@app.route("/count", methods=["GET"])
def count():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
