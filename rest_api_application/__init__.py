"""
Flask Application Configuration and Initialization

This module initializes the Flask application and sets up essential configurations such as
database connection, JWT authentication, and API routing.
It loads environment variables from a .env file using the python-dotenv library.
The SQLAlchemy extension is used for database management and migration.
JWTManager is configured for handling JSON Web Tokens for authentication.
Additionally, a Blueprint for login views is registered with the Flask application.

Attributes:
    app: The Flask application instance.
    api: The Flask-RESTful API instance.
    jwt: The JWTManager instance for JSON Web Token handling.
    db: The SQLAlchemy database instance.
    login_blueprint: The Blueprint for login views.
"""

import os
from os import getenv
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Api

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = getenv('JWT_SECRET_KEY')
api = Api(app)
jwt = JWTManager(app)


app.config['SECRET_KEY'] = getenv('SECRET_KEY')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

db = SQLAlchemy(app)
Migrate(app,db)

from rest_api_application.login.views import login_blueprint
app.register_blueprint(login_blueprint)
