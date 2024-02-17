#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
flask_app = Flask(__name__)


@flask_app.route("/states_list", strict_slashes=False)
def state():
    """list"""
    states = storage.all("State")
    return render_template("7-states_list.py", states=states)


@flask_app.teardown_appcontext
def teardown(exc):
    """close"""
    storage.close()


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)
