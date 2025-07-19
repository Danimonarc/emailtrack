from flask import Flask, request, send_file
from datetime import datetime

app = Flask(__name__)

@app.route('/track.png')
def track():
    with open("access.log", "a") as f:
        f.write(f"[{datetime.now()}] IP: {request.remote_addr}, UA: {request.headers.get('User-Agent')}\n")
    return send_file("pixel.png", mimetype='image/png')
