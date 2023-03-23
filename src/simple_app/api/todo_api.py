from flask import request

from simple_app.db import db
from simple_app.models.todo import Todo


def add_todo():
    action = request.json.get("action", None)
    if action is None:
        return "action not found", 400
    todo = Todo(action=action)
    return todo


def list_todo():
    todos = db.session.execute(db.select(Todo)).scalars()
    for t in todos:
        print(t)
    return todos
