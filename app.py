from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Scraper SEACE listo", "status": "ok"})

@app.route("/run-scraper", methods=["GET"])
def run_scraper():
    try:
        result = subprocess.run(
            ["python3", "seace_scraper_selenium.py"],
            check=True,
            capture_output=True,
            text=True
        )
        return jsonify({"status": "success", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({
            "status": "error",
            "message": e.stderr or str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
