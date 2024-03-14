from rest_api_application  import db

class EventParticipation(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    events_id = db.Column(db.Integer, db.ForeignKey('events.id')) 