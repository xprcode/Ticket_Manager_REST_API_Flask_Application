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
