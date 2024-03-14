from flask import Blueprint,  session
from flask_login import login_user, LoginManager
from werkzeug.security import check_password_hash
from flask import jsonify
from flask import request
from flask_jwt_extended import create_access_token

from rest_api_application.models.user import User
from rest_api_application import app

login_blueprint = Blueprint('login',__name__, template_folder='templates')

login_manager = LoginManager(app)
login_manager.login_view = 'login.login'

@login_blueprint.route('/login', methods = ['POST'])
def login():

    username = request.json.get("username", None)
    password = request.json.get("password", None)
  
    user = User.query.filter(User.name == username).first()
    
    if user is not None and check_password_hash(user.password, password):
        session['user_id'] = user.id
        login_user(user)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

