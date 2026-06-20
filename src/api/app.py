from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import os
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

VERSION = os.getenv("VERSION", "v1")
ERROR_RATE = float(os.getenv("ERROR_RATE", "0"))


@app.route("/")
def index():
    if random.random() < ERROR_RATE:
        return {
            "status": "error",
            "version": VERSION
        }, 500

    return {
        "status": "ok",
        "version": VERSION
    }, 200


@app.route("/healthz")
def healthz():
    return {
        "status": "healthy"
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)