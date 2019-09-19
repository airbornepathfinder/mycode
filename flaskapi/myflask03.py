#!/usr/bin/env python3

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello {} Guest".format(guest)

@app.route("/user/<name>")
def hello_user(name):
    if name =="admin":
        return redirect(url_for("hello_name"))
    else:
        return redirect(url_for("hello_guest",guest = name))

#app.add_url_rule("/hello", "hello", hello_name)

if __name__ == "__main__":
    app.run(port=5006, debug = True)
