from flask import Flask, render_template
import datetime

app = Flask(__name__)

posts = [
    {"title": "djksjd", "body": "asdjasdlljdajdsl"},
    {"title": "djk21332132sjd", "body": "asdj123231asdlljdajdsl"},
]


@app.route("/")
def index():
    context = {"time": datetime.datetime.now(), "posts": posts}
    return render_template('index.html', **context)