"""
Events Model

This module defines the Events model for the application.

"""
from rest_api_application import db

class Events(db.Model):
    """
    Events Model Class

    Represents an event in the application.

    Attributes:
        id (int): The unique identifier for the event.
        event_name (str): The name of the event.
        event_adress (str): The address of the event.
        event_date (DateTime): The date of the event.
        event_events (relationship): Relationship to EventParticipation
        indicating user participation in the event.
    """
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50))
    event_adress = db.Column(db.String(50))
    event_date = db.Column(db.DateTime)
    event_events = db.relationship('EventParticipation', backref='events', lazy='dynamic')
