from rest_api_application  import db


class Events(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50))
    event_adress = db.Column(db.String(50))
    event_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

   