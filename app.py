from flask import Flask, render_template, session, request
from flask_session import Session
from fake_useragent import UserAgent
import requests, json
import content_aggregator
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {
    "User-Agent": ua.random
}

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST', 'GET'])
def api():
    if(request.method == 'GET'):
        return render_template('index.html', error_messages="Request Method Get Not Allowed, Please Enter Part Name!")
    session["category"] = request.form.get("Category-Options")
    session["part_name"] = request.form.get("partname")
    part_list = content_aggregator.get_part_details(session["part_name"],session["category"])
    if(part_list == []):
        return render_template("index.html", error_message = f'No Part Named {session["part_name"]} Found')
    return render_template('parts.html')

@app.route('/check_static')
def check_static():
    return "Static files can be accessed."

if __name__ == '__main__':
    app.run(debug=True)
