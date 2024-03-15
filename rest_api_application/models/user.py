"""
User Model

This module defines the User model for the application.

"""
from flask_login import UserMixin
from rest_api_application  import db

class User(db.Model, UserMixin):
    """
    User Model Class

    Represents a user in the application.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The username of the user.
        password (str): The password of the user.
        email (str): The email address of the user.
        user_event (relationship): Relationship to EventParticipation 
        indicating events associated with the user.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(50))
    user_event = db.relationship('EventParticipation', backref='user', lazy='dynamic')
  