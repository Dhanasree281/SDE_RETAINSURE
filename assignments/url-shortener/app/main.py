
from flask import Flask, request, jsonify, redirect
from datetime import datetime
import string, random
from threading import Lock

app = Flask(__name__)
url_store = {}  # { short_code: { url, created_at, clicks } }
lock = Lock()

import random, string
url = request.json["url"]  # risky if "url" doesn't exist


def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print(f"[INFO] Shortened {url} to {short_code}")


@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    url = data.get("url")
    # your logic to shorten the URL
    return jsonify({"short_url": "http://short.ly/abc123"})


@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)