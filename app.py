from werkzeug.security import generate_password_hash
from rest_api_application import app, db, api

from rest_api_application.models.user import User
from rest_api_application.models.events import Events
from rest_api_application.models.eventparticipation import EventParticipation


from rest_api_application.event.event import Event
api.add_resource(Event, '/event/<int:user_id>/<int:event_id>')

@app.route('/')
def index():
    return 'ok'


if __name__ == "__main__":
    app.run()