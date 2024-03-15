from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from rest_api_application import db
from rest_api_application.models.events import Events
from rest_api_application.models.eventparticipation import EventParticipation
from rest_api_application.models.user import User

class UserEvent(Resource):

    @jwt_required()
    def get(self, user_id, event_id=None):
        if not user_id:
            return {'error': 'User not found'}, 400

        user = User.query.filter(User.id == user_id).first()
        if not user:
            return {'error': 'User not found'}, 404

        if not event_id:
            participations = EventParticipation.query.filter_by(user_id=user_id).all()
            if not participations:
                return {'error': 'User has not eny events added.'}, 400
            event_ids = [participation.events_id for participation in participations]

            events = Events.query.filter(Events.id.in_(event_ids)).all()
            all_event = [{
            'event_name': event.event_name,
            'event_adress': event.event_adress,
            'event_date': event.event_date
            } for event in events]
            return jsonify({'events': all_event})

        participation = EventParticipation.query.filter_by( user_id=user_id,
                                                            events_id=event_id).first()
        if participation:
            event = Events.query.get(event_id)
            particular_event = {
                'event_name': event.event_name,
                'event_adress': event.event_adress,
                'event_date': event.event_date
            }

            return jsonify({'event': particular_event})
        return {'error': 'Event not found'}, 404