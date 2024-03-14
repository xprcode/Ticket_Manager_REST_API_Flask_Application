from rest_api_application  import db
from rest_api_application.models.eventparticipation import EventParticipation

class Events(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50))
    event_adress = db.Column(db.String(50))
    event_date = db.Column(db.DateTime)
    event_events = db.relationship('EventParticipation', backref='events', lazy='dynamic')

   