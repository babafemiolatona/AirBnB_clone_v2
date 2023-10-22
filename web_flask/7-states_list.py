#!/usr/bin/python3
"""Starts a Flash Web Application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
