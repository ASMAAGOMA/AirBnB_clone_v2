#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
flask_app = Flask(__name__)


@flask_app.route("/", strict_slashes=False)
def homePage():
    """Hello HBNB"""
    return "Hello HBNB!"


@flask_app.route("/hbnb", strict_slashes=False)
def homePage2():
    """HBNB"""
    return "HBNB"


@flask_app.route("/c/<text>", strict_slashes=False)
def homePage3(text):
    """HBNB"""
    spaces_word = text.replace('_', ' ')
    final = f"c {spaces_word}"
    return final


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)
