from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/noivos")
def noivos():
    return render_template("noivos.html")


@app.route("/igreja")
def igreja():
    return render_template("igreja.html")


@app.route("/recepcao")
def recepcao():
    return render_template("recepcao.html")


@app.route("/ramalhetes")
def ramalhetes():
    return render_template("ramalhetes.html")
