"""
Login Views

This module provides views for user authentication, including login functionality.

"""
from flask import Blueprint, session, jsonify, request
from flask_login import login_user, LoginManager
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from rest_api_application.models.user import User
from rest_api_application import app

login_blueprint = Blueprint('login',__name__, template_folder='templates')

login_manager = LoginManager(app)
login_manager.login_view = 'login.login'

@login_blueprint.route('/login', methods = ['POST'])
def login():
    """
    Log in user and generate access token.

    Returns:
        JSON: Access token if login is successful, error message otherwise.
    """

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400
    user = User.query.filter(User.name == username).first()

    if user is not None and check_password_hash(user.password, password):
        session['user_id'] = user.id
        login_user(user)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username aaor password"}), 401
