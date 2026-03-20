from flask import Flask, jsonify
import socket, datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Mock AMF",
        "status": "running",
        "time": str(datetime.datetime.now()),
        "host": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

app.run(host="0.0.0.0", port=8080)
