from flask_login import UserMixin

from rest_api_application  import db


class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    events = db.relationship('Events', backref='user', lazy='dynamic')
    