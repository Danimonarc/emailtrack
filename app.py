from flask import Flask, request, send_file
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import datetime

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

@app.route('/track.png')
def track():
    # Ahora sí, request.remote_addr tiene la IP real del cliente
    real_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    with open("access.log", "a") as f:
        f.write(f"[{datetime.now()}] IP: {real_ip}, UA: {user_agent}\n")

    return send_file("1x1.png", mimetype='image/png')

@app.route('/logs')
def logs():
    with open("access.log", "r") as f:
        return "<pre>" + f.read() + "</pre>"
