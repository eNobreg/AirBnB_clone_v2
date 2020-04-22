#!/usr/bin/python3
"""
Module for running a web flask application
"""

from flask import Flask, request, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states")
@app.route("/states/<sid>")
def list_states(sid=None, strict_slashes=False):
    states = storage.all(State)
    if sid is not None:
        sid = "State.{}".format(sid)
    return render_template("9-states.html", states=states, id=sid)


@app.teardown_appcontext
def error_handler(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
