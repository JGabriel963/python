from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///floricultura.sqlite3"
db = SQLAlchemy()
db.init_app(app)

from app import routes
