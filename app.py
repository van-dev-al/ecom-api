from flask import Flask, render_template, jsonify, request
import requests, json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Dữ liệu JSON mẫu
    data = [
        {"title": "Item 1", "description": "Description for item 1.", "price": "$10.99"},
        {"title": "Item 2", "description": "Description for item 2.", "price": "$12.99"},
        {"title": "Item 3", "description": "Description for item 3.", "price": "$14.99"},
        {"title": "Item 4", "description": "Description for item 4.", "price": "$16.99"},
        {"title": "Item 5", "description": "Description for item 5.", "price": "$18.99"},
        {"title": "Item 6", "description": "Description for item 6.", "price": "$20.99"},
        {"title": "Item 7", "description": "Description for item 7.", "price": "$22.99"},
        {"title": "Item 8", "description": "Description for item 8.", "price": "$24.99"},
        {"title": "Item 9", "description": "Description for item 9.", "price": "$26.99"},
        {"title": "Item 10", "description": "Description for item 10.", "price": "$28.99"},
        {"title": "Item 3", "description": "Description for item 3.", "price": "$14.99"},
        {"title": "Item 4", "description": "Description for item 4.", "price": "$16.99"},
        {"title": "Item 5", "description": "Description for item 5.", "price": "$18.99"},
        {"title": "Item 6", "description": "Description for item 6.", "price": "$20.99"},
        {"title": "Item 7", "description": "Description for item 7.", "price": "$22.99"},
        {"title": "Item 8", "description": "Description for item 8.", "price": "$24.99"},
        {"title": "Item 9", "description": "Description for item 9.", "price": "$26.99"},
        {"title": "Item 10", "description": "Description for item 10.", "price": "$28.99"},
        {"title": "Item 3", "description": "Description for item 3.", "price": "$14.99"},
        {"title": "Item 4", "description": "Description for item 4.", "price": "$16.99"},
        {"title": "Item 5", "description": "Description for item 5.", "price": "$18.99"},
        {"title": "Item 6", "description": "Description for item 6.", "price": "$20.99"},
        {"title": "Item 7", "description": "Description for item 7.", "price": "$22.99"},
        {"title": "Item 8", "description": "Description for item 8.", "price": "$24.99"},
        {"title": "Item 9", "description": "Description for item 9.", "price": "$26.99"},
        {"title": "Item 10", "description": "Description for item 10.", "price": "$28.99"},
        {"title": "Item 3", "description": "Description for item 3.", "price": "$14.99"},
        {"title": "Item 4", "description": "Description for item 4.", "price": "$16.99"},
        {"title": "Item 5", "description": "Description for item 5.", "price": "$18.99"},
        {"title": "Item 6", "description": "Description for item 6.", "price": "$20.99"},
        {"title": "Item 7", "description": "Description for item 7.", "price": "$22.99"},
        {"title": "Item 8", "description": "Description for item 8.", "price": "$24.99"},
        {"title": "Item 9", "description": "Description for item 9.", "price": "$26.99"},
        {"title": "Item 10", "description": "Description for item 10.", "price": "$28.99"},
    ]

    # Chuyển đổi dữ liệu thành chuỗi JSON
    json_data = json.dumps(data, indent=2)

    # Render template và truyền dữ liệu JSON vào
    return render_template('index.html', data=json_data)


@app.route('/api')
def api():
    return "api"

@app.route('/check_static')
def check_static():
    return "Static files can be accessed."

if __name__ == '__main__':
    app.run(debug=True)
