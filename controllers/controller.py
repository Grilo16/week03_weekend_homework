from app import app
from flask import render_template


@app.route("/")
def homepage():
    return render_template("index.html", page_title = "Page title", page_h1 = "Page h1") 