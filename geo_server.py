from flask import Flask, request
import requests

app = Flask(__name__)

# Вставь свой токен сюда:
IPINFO_TOKEN = "4e9a9682e56c8b"

@app.route('/')
def get_geo():
    # Получаем IP пользователя
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Запрашиваем данные с IPinfo
    response = requests.get(f"https://ipinfo.io/{user_ip}?token={IPINFO_TOKEN}")
    data = response.json()

    # Формируем вывод
    return f"""
        <h2>IP: {user_ip}</h2>
        <p>Город: {data.get('city')}</p>
        <p>Регион: {data.get('region')}</p>
        <p>Страна: {data.get('country')}</p>
        <p>Провайдер: {data.get('org')}</p>
        <p>Локация (широта,долгота): {data.get('loc')}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
