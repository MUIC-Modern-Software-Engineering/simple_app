import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from simple_app.api import todo_api
from simple_app.db import db

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI", None)
cors = CORS(app)

with app.app_context():
    db.init_app(app)
    db.create_all()

migrate = Migrate(app, db)


@app.route("/")
def index():
    return "hello world222"


app.add_url_rule("/todo", methods=["GET"], view_func=todo_api.list_todo)
app.add_url_rule("/add-random-todo", methods=["GET"], view_func=todo_api.add_random_todo)
