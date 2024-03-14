from flask import Flask
from werkzeug.security import generate_password_hash
from rest_api_application import app, db, api
from rest_api_application.models.user import User
from rest_api_application.models.events import Events


from rest_api_application.event.event import Event
api.add_resource(Event, '/puppy/<string:name>/<string:rasa>')
# api.add_resource(Event,'/puppy/<string:name>')



@app.route('/')
def index():
    
    return 'ok'



if __name__ == "__main__":
    app.run()