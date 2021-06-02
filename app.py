from flask import Flask, render_template
import datetime
import requests
import json

app = Flask(__name__)

posts = json.loads(requests.get("https://jsonplaceholder.typicode.com/posts").text)


@app.route("/")
def index():
    context = {"time": datetime.datetime.now(), "posts": posts}
    return render_template('index.html', **context)