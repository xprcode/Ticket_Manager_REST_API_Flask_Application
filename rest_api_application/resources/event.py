from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from rest_api_application import db
from rest_api_application.models.events import Events
from rest_api_application.models.eventparticipation import EventParticipation
from rest_api_application.models.user import User
from rest_api_application.email_manager.main import send_by_EmailSender

class Event(Resource):

    @jwt_required()
    def post(self, user_id, event_id):

        user_id = request.json.get('user_id')
        event_id = request.json.get('event_id')
        if not user_id or not event_id:
            return {'error': 'User or event not found'}, 400

        user = User.query.filter(User.id == user_id).first()
        event = Events.query.filter(Events.id == event_id).first()
        if not user or not event:
            return {'error': 'User or event not found'}, 404

        new_event_participation = EventParticipation(
            user_id=user.id,
            events_id=event.id
            )

        db.session.add(new_event_participation)
        db.session.commit()
        send_by_EmailSender(user.id, event.id)
        return {'message': 'Participation recorded successfully'}, 201
