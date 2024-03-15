"""
User and Event Entity

This module provides functionality for retrieving user and event
information and creating an entity object containing relevant details.

"""
from collections import namedtuple
from rest_api_application.models.user import User
from rest_api_application.models.events import Events

Entity = namedtuple('Entity', 'name email event_name event_adress event_data')

def get_user_and_event(user_id, event_id):
    """
    Get user and event information and create an entity object.

    Args:
        user_id (int): The ID of the user.
        event_id (int): The ID of the event.

    Returns:
        Entity: An entity object containing user and event details.
    """

    user = User.query.filter(User.id == user_id).first()
    event = Events.query.filter(Events.id == event_id).first()
    user_and_event = Entity(user.name,
                            user.email,
                            event.event_name,
                            event.event_adress,
                            event.event_date)
    return user_and_event
