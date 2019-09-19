#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"
app.add_url_rule("/hello", "hello", hello_world)

if __name__ == "__main__":
    app.run(port=5006)

