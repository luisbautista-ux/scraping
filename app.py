from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Scraper SEACE listo", "status": "ok"})

@app.route("/run-scraper", methods=["GET"])
def run_scraper():
    try:
        # Ejecuta tu script principal
        subprocess.run(["python", "seace_scraper_playwright_v19.py"], check=True)
        return jsonify({"status": "success", "message": "Scraping ejecutado correctamente"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
