from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Hello")

@app.route("/customise")
def customise():
    return render_template("customise.html", title="Customise")

@app.route("/focus")
def focus():
    return render_template("focus.html", title="Focus Session")
    