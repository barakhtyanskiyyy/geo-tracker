from flask import Flask, request
import requests
import os

app = Flask(__name__)
IPINFO_TOKEN = os.getenv("4e9a9682e56c8b")

@app.route('/')
def get_geo():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if not IPINFO_TOKEN:
        return "Ошибка: токен IPinfo не указан."

    response = requests.get(f"https://ipinfo.io/{user_ip}?token={IPINFO_TOKEN}")
    data = response.json()

    city = data.get('city', 'Нет данных')
    region = data.get('region', 'Нет данных')
    country = data.get('country', 'Нет данных')
    org = data.get('org', 'Нет данных')
    loc = data.get('loc', 'Нет данных')

    return f"""
    <h1>IP: {user_ip}</h1>
    <p>Город: {city}</p>
    <p>Регион: {region}</p>
    <p>Страна: {country}</p>
    <p>Провайдер: {org}</p>
    <p>Локация (широта,долгота): {loc}</p>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
