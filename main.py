'''
Bones of a skeleton website. 

Purpose: Gain familiarity with website construction 
Goal: Get a working connection between a URL and code
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")


if __name__ == "__main__":
    app.run(debug=True)
