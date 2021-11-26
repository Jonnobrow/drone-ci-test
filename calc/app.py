# -*- coding: utf-8 -*-
from flask import Flask, request
from markupsafe import escape
import calc
import os

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome to calculator app, try /add/3/4 or /sub/2/1"


@app.route("/add/<int:x>/<int:y>")
@app.route("/sub/<int:x>/<int:y>")
def calculations(x, y):
    rule = request.url_rule
    response = "Failed to calculate answer"
    if "add" in rule.rule:
        ans = calc.add(x, y)
        response = escape(f"The answer to {x} + {y} = {ans}")
    elif "sub" in rule.rule:
        ans = calc.sub(x, y)
        response = escape(f"The answer to {x} - {y} = {ans}")
    return response


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8080))
    debug = bool(os.getenv("DEBUG", False))
    app.run(host, port, debug=debug)
