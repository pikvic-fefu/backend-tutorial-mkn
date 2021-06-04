from flask import Flask, render_template
import datetime
import requests
import json

app = Flask(__name__)

def get_posts():
    posts = json.loads(requests.get("https://jsonplaceholder.typicode.com/posts").text)
    users = json.loads(requests.get("https://jsonplaceholder.typicode.com/users").text)
    comments = json.loads(requests.get("https://jsonplaceholder.typicode.com/comments").text)

    for post in posts:
        for user in users:
            if post["userId"] == user["id"]:
                post["user"] = user["name"]
        post["comments"] = []
        for comment in comments:
            if post["id"] == comment["postId"]:
                post["comments"].append(comment)
        post["comments_count"] = len(post["comments"])
    return posts

@app.route("/")
def index():
    posts = get_posts()
    context = {"time": datetime.datetime.now(), "posts": posts}
    return render_template('index.html', **context)