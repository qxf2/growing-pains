"""
A simple Flask app that fetches you a random quote
"""
import csv
import os
import random
import flask
from flask import render_template

app = flask.Flask(__name__)
INPUT_DATA = os.path.join(os.path.dirname(__file__), 'problems.csv')

def get_a_pain():
    """Return a list of growing pains"""
    with open(INPUT_DATA, newline='') as csvfile:
        all_pains = list(csv.reader(csvfile))

    return random.choice(all_pains)

@app.route("/")
def home_page():
    """this is the home page of my web app"""
    return render_template('index.html')

@app.route("/get-random-pain")
def get_random_quote():
    """Return a random quote"""
    pain = get_a_pain()
    pain = {'summary':pain[0], 'description':pain[1]}

    return flask.jsonify(pain)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6464, debug=True)
