import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def health_check():
    return jsonify({
        "status": "online",
        "system": "A7-AXIS Sentinel Engine",
        "protocol": "Lazarus-Active"
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "active", "protocol": "A7-AXIS-Lazarus-Protocol", "benchmark": "11%"})

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "telemetry": "green"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
