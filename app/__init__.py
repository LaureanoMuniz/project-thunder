from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

# Load configuration from a separate config file (e.g., config.py)
app.config.from_object('config')

# Initialize the SQLAlchemy database


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from app import routes