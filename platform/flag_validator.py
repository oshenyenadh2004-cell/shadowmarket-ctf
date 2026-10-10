from flask import Flask, request, jsonify
import hashlib
from datetime import datetime

app = Flask(__name__)

# Correct flags are stored as SHA-256 hashes, never in plaintext,
# so inspecting this source file does not reveal the answers.
CORRECT_FLAG_HASHES = {
    "stage1": hashlib.sha256(b"SHADOWMKT{DarkK1ng99}").hexdigest(),
    "stage2": hashlib.sha256(b"SHADOWMKT{DarkNet_Chat_0x99}").hexdigest(),
    "stage3": hashlib.sha256(b"SHADOWMKT{SRVNODE7EAST}").hexdigest(),
    "stage4": hashlib.sha256(b"SHADOWMKT{SQL_BYP4SS_SUCC3SS}").hexdigest(),
    "stage5": hashlib.sha256(b"SHADOWMKT{UMBRA_NODE_9}").hexdigest(),
    "stage6": hashlib.sha256(b"SHADOWMKT{TAKEDOWN_CONFIRMED}").hexdigest(),
}

LOG_FILE = "validation_log.txt"


def log_attempt(stage, submitted_flag, correct):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().isoformat()
        result = "CORRECT" if correct else "INCORRECT"
        f.write(f"{timestamp} | stage={stage} | flag={submitted_flag} | result={result}\n")


@app.route("/submit", methods=["POST"])
def submit_flag():
    data = request.get_json(silent=True)
    if not data or "stage" not in data or "flag" not in data:
        return jsonify({"error": "Missing 'stage' or 'flag' in request"}), 400

    stage = data["stage"]
    submitted_flag = data["flag"]

    if stage not in CORRECT_FLAG_HASHES:
        return jsonify({"error": f"Unknown stage '{stage}'"}), 404

    submitted_hash = hashlib.sha256(submitted_flag.encode()).hexdigest()
    is_correct = submitted_hash == CORRECT_FLAG_HASHES[stage]

    log_attempt(stage, submitted_flag, is_correct)

    if is_correct:
        return jsonify({"result": "correct", "message": f"{stage} solved!"}), 200
    else:
        return jsonify({"result": "incorrect"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001)
