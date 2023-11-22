from flask import Flask, render_template, request

app = Flask(__name__)

contents = []
diarys = []

# localhost:5000/route
# Running with - flask --app filename run --debug


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
