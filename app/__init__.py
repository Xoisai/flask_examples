from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# Read in configuration file
app.config.from_object(Config)

# Set up database objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User login functionality
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
