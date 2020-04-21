#!/usr/bin/python3
"""
Module
"""

from models import storage
from models.state import State
from flask import Flask, request, render_template, abort


app = Flask(__name__)


@app.route("/cities_by_states")
def state_cities(strict_slashes=False):
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tear(errors):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
