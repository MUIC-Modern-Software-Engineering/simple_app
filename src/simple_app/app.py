import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from simple_app.api import todo_api
from simple_app.db import db
from simple_app.models.todo import Todo

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DB_URI', None)

with app.app_context():
    db.init_app(app)
    db.create_all()
    # todo = Todo(action='hello me')
    # db.session.add(todo)
    # db.session.commit()

migrate = Migrate(app, db)


@app.route("/")
def index():
    return 'hello world'


app.add_url_rule("/todo", methods=["GET"], view_func=todo_api.list_todo)
app.add_url_rule("/todo", methods=["POST"], view_func=todo_api.add_todo)
