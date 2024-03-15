"""
EventParticipation Model

This module defines the EventParticipation model for the application.

"""
from rest_api_application  import db

class EventParticipation(db.Model):
    """
    EventParticipation Model Class

    Represents the participation of a user in an event.

    Attributes:
        id (int): The unique identifier for the event participation record.
        user_id (int): The ID of the user participating in the event.
        events_id (int): The ID of the event in which the user is participating.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    events_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    