from project import app, db
from flask import render_template, request, redirect, url_for
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
    page = request.args.get("page", 1, type=int)
    per_page = 2
    all_books = Book.query.paginate(page=page, per_page=per_page)
    return render_template("books.html", books=all_books)


@app.route("/add_book", methods=["POST", "GET"])
def add_book():
    name = request.form.get("name")
    description = request.form.get("description")
    value = request.form.get("value")
    if request.method == "POST":
        book = Book(name, description, value)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("list_books"))
    return render_template(
        "new_book.html",
    )


@app.route("/<int:id>/update_book", methods=["POST", "GET"])
def update_book(id):
    # select * from book where id = 2
    book_db = Book.query.filter_by(id=id).first()
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        value = request.form["value"]

        Book.query.filter_by(id=id).update(
            {"name": name, "description": description, "value": value}
        )

        db.session.commit()
        return redirect(url_for("list_books"))
    return render_template(
        "update_book.html",
        book=book_db,
    )


@app.route("/<int:id>/remove_book")
def remove_book(id):
    book_db = Book.query.filter_by(id=id).first()
    db.session.delete(book_db)
    db.session.commit()
    return redirect(url_for("list_books"))
