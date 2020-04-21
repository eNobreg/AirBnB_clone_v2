#!/usr/bin/python3
'''
A small web application to print states
'''
from models import storage
from models.state import State
from flask import Flask, request, escape, render_template, abort

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    storage.close()


@app.route("/states_list")
def list_states(static_slashes=False):
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
