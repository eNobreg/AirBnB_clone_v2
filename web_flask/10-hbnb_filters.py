#!/usr/bin/python3
"""
Flask application for serving website
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, request, render_template, abort


app = Flask(__name__)


@app.teardown_appcontext
def error_handler(error):
    """
    Removes SQLAlchemy session
    """
    storage.close()


@app.route("/hbnb_filters")
def serve_hbhb_static(strict_slashes=False):
    """
    Servers static flask web app
    """
    states = storage.all(State).values()
    ameni = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states, ameni=ameni)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
