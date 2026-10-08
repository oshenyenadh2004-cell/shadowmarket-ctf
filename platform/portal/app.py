from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "dev-key-change-for-production"

VALIDATOR_URL = "http://flag-validator:6001/submit"

STAGES = {
    "stage1": {"title": "The Vendor's Footprint", "domain": "OSINT", "difficulty": "Easy",
               "folder": "stage1-osint", "files": ["vendor_post.jpg"], "type": "static"},
    "stage2": {"title": "Buried in the Upload", "domain": "Steganography", "difficulty": "Easy",
               "folder": "stage2-stego", "files": ["upload_42.jpg"], "type": "static"},
    "stage3": {"title": "Coded Correspondence", "domain": "Cryptography", "difficulty": "Moderate",
               "folder": "stage3-crypto", "files": ["chatlog.txt"], "type": "static"},
    "stage4": {"title": "The Mirror Login", "domain": "Web Security", "difficulty": "Moderate",
               "type": "web", "url": "http://localhost:5000"},
    "stage5": {"title": "The Seized Drive", "domain": "Digital Forensics", "difficulty": "Moderate-Hard",
               "folder": "stage5-forensics", "files": ["seized_drive.img"], "type": "static"},
    "stage6": {"title": "Takedown", "domain": "Networking", "difficulty": "Hard",
               "folder": "stage6-network", "files": ["takedown.pcap"], "type": "static"},
}

solved = set()

@app.route("/")
def index():
    return render_template("index.html", stages=STAGES, solved=solved)

@app.route("/stage/<stage_id>")
def stage_detail(stage_id):
    stage = STAGES.get(stage_id)
    if not stage:
        return "Stage not found", 404
    return render_template("stage.html", stage_id=stage_id, stage=stage, is_solved=(stage_id in solved))

@app.route("/download/<stage_id>/<path:filename>")
def download(stage_id, filename):
    stage = STAGES.get(stage_id)
    if not stage or stage["type"] != "static":
        return "Not found", 404
    return send_from_directory(f"static/{stage['folder']}", filename, as_attachment=True)

@app.route("/submit/<stage_id>", methods=["POST"])
def submit(stage_id):
    flag = request.form.get("flag", "")
    try:
        resp = requests.post(VALIDATOR_URL, json={"stage": stage_id, "flag": flag}, timeout=5)
        result = resp.json()
    except Exception as e:
        flash(f"Validator unreachable: {e}")
        return redirect(url_for("stage_detail", stage_id=stage_id))

    except Exception as e:
        flash(f"System error — validator unreachable: {e}", "error")

    if result.get("result") == "correct":
        solved.add(stage_id)
        flash(f"Correct! {stage_id} marked as solved.")
    else:
        flash("Incorrect flag, try again.")
    return redirect(url_for("stage_detail", stage_id=stage_id))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

    if result.get("result") == "correct":
        solved.add(stage_id)
        flash(f"Access granted — {stage_id} cleared.", "success")
    else:
        flash("Access denied — incorrect key.", "error")
