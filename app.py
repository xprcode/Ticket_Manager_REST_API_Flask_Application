from flask import Flask
from werkzeug.security import generate_password_hash
from rest_api_application import app, db, api
from rest_api_application.models.user import User
from rest_api_application.models.events import Events
from datetime import datetime

from rest_api_application.event.event import Event
api.add_resource(Event, '/puppy/<string:name>/<string:rasa>')
# api.add_resource(Event,'/puppy/<string:name>')



@app.route('/')
def index():
    new_user = User(
            name='Joe',
            password=generate_password_hash("newpassword"),
            email="xprtsw@o2.pl"

        )
    db.session.add(new_user)
    db.session.commit()
    print('added')
    return 'ok'



if __name__ == "__main__":
    app.run()