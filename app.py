from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Scraper SEACE listo"})

@app.route("/scrape", methods=["GET"])
def run_scraper():
    try:
        # Ejecuta tu script principal
        result = subprocess.run(
            ["python", "seace_scraper_playwright_v19.py"],
            capture_output=True,
            text=True,
            timeout=900  # 15 minutos máx
        )
        return jsonify({
            "status": "success" if result.returncode == 0 else "error",
            "output": result.stdout[-1500:],  # últimas líneas del log
            "error": result.stderr
        })
    except subprocess.TimeoutExpired:
        return jsonify({"status": "error", "message": "Timeout: el scraping tomó demasiado tiempo"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
