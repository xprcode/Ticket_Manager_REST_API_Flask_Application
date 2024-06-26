"""
Flask Application Configuration and Routing

This module initializes the Flask application and sets up the API routing 
for the ticket manager web application. It imports the necessary resources 
for managing events and user events and adds corresponding endpoints to the Flask API.

Attributes:
    app: The Flask application instance.
    api: The Flask-RESTful API instance.

Routes:
    - /events/<int:user_id>/<int:event_id>: Endpoint for managing events.
    - /user_event/<int:user_id>: Endpoint for retrieving user events 
    and adding events to a user's list.
    - /user_event/<int:user_id>/<int:event_id>: Endpoint for retrieving 
    a specific event associated with a user.

"""

from rest_api_application import app, api
from rest_api_application.resources.event import Event
from rest_api_application.resources.user_event import UserEvent

# Adding event to user portfolio - POST method.
api.add_resource(Event, '/events/<int:user_id>/<int:event_id>')
# Getting all events or particular event from the user portfolio - GET method
api.add_resource(UserEvent, '/user-events/<int:user_id>', '/user-events/<int:user_id>/<int:event_id>')


if __name__ == "__main__":
    app.run()
