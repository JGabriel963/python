from project import app
from flask import render_template, request
from project.list_movies import result_movies
from project.book import Book

contents = []
diarys = []


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if request.form.get("content"):
            contents.append(request.form.get("content"))
            ### Limpar input
    return render_template("index.html", contents=contents)


@app.route("/diary", methods=["GET", "POST"])
def diary():
    if request.method == "POST":
        if request.form.get("student") and request.form.get("note"):
            student = request.form.get("student")
            note = request.form.get("note")
            diarys.append({"student": student, "note": note})
    return render_template("about.html", diarys=diarys)


@app.route("/movies/<property>")
def list_movies(property):
    return render_template("movies.html", movies=result_movies(property))


@app.route("/books")
def list_books():
    return render_template("books.html", books=Book.query.all())
