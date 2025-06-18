from flask import Flask, request
import requests

app = Flask(__name__)

IPINFO_TOKEN = "4e9a9682e56c8b"

@app.route("/")
def get_geo():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print("📡 Новый переход с IP:", user_ip)
    
    response = requests.get(f"https://ipinfo.io/{user_ip}?token={IPINFO_TOKEN}").json()

    city = response.get("city")
    region = response.get("region")
    country = response.get("country")
    org = response.get("org")
    loc = response.get("loc")

    return f"""
    <h1>IP: {user_ip}</h1>
    <p>Город: {city}</p>
    <p>Регион: {region}</p>
    <p>Страна: {country}</p>
    <p>Провайдер: {org}</p>
    <p>Локация (широта,долгота): {loc}</p>
    """
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
