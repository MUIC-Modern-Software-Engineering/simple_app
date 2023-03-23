import os

from flask_migrate import Migrate
from flask_script import Manager

from simple_app.app import app
from simple_app.db import db

app.config.from_object(os.environ["APP_SETTINGS"])

migrate = Migrate(app, db)
manager = Manager(app)


if __name__ == "__main__":
    manager.run()
