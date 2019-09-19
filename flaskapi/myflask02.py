#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")

def hello_name(name):
    return "Hello {}".format(name)

app.add_url_rule("/hello", "hello", hello_name)

if __name__ == "__main__":
    app.run(port=5006, debug = True)
