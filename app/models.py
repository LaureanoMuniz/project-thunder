
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from app import app,db
from flask_migrate import Migrate
import config

app.config.from_object(config)




migrate = Migrate(app, db)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"


