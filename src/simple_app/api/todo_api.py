from secrets import token_hex

from simple_app.db import db
from simple_app.models.todo import Todo


def add_random_todo():
    todo = Todo(action=token_hex(8))
    db.session.add(todo)
    db.session.commit()
    return {"id": todo.id, "action": todo.action}


def list_todo():
    todos = db.session.execute(db.select(Todo)).scalars()
    return [t.action for t in todos]
