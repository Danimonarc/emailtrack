from flask import Flask, request, send_file
from datetime import datetime

app = Flask(__name__)

@app.route('/track.png')
def track():
    # Obtener la IP real del cliente
    real_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Log del acceso
    with open("access.log", "a") as f:
        f.write(f"[{datetime.now()}] IP: {real_ip}, UA: {request.headers.get('User-Agent')}\n")

    return send_file("1x1.png", mimetype='image/png')

# Opcional: para ver logs desde el navegador
@app.route('/logs')
def logs():
    with open("access.log", "r") as f:
        return "<pre>" + f.read() + "</pre>"
