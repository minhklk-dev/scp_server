from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load or create the database
try:
    with open("database.json", "r") as f:
        db = json.load(f)
except:
    db = {"players": 0}

@app.route("/played", methods=["POST"])
def played():
    db["players"] += 1
    with open("database.json", "w") as f:
        json.dump(db, f)
    return {"status": "ok", "players": db["players"]}

@app.route("/count", methods=["GET"])
def count():
    return jsonify(db)

app.run(port=5000)
