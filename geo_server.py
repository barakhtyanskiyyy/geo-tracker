from flask import Flask, request
import requests
import os

app = Flask(__name__)
IPINFO_TOKEN = os.getenv("4e9a9682e56c8b")

@app.route('/')
def get_geo():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    if not IPINFO_TOKEN:
        return "Ошибка: IPINFO_TOKEN не задан."

    response = requests.get(f"https://ipinfo.io/{user_ip}?token={IPINFO_TOKEN}")
    data = response.json()

    city = data.get('city')
    region = data.get('region')
    country = data.get('country')
    org = data.get('org')
    loc = data.get('loc')

    return f"""
    <h1>IP: {user_ip}</h1>
    <p>Город: {city}</p>
    <p>Регион: {region}</p>
    <p>Страна: {country}</p>
    <p>Провайдер: {org}</p>
    <p>Локация: {loc}</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
