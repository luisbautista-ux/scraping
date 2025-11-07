from flask import Flask, jsonify
import subprocess, threading

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Scraper SEACE listo", "status": "ok"})

def run_scraper_async():
    # Ejecuta el script sin bloquear el hilo principal
    subprocess.run(
        ["python3", "seace_scraper_selenium.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

@app.route("/run-scraper", methods=["GET"])
def run_scraper():
    # Lanza el scraper en un hilo separado
    threading.Thread(target=run_scraper_async).start()
    return jsonify({
        "status": "running",
        "message": "Scraper iniciado en segundo plano. Verifica logs en Render."
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
