from simple_app.db import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String, nullable=False)
