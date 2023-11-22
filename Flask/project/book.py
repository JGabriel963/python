from project import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    value = db.Column(db.Integer)

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
