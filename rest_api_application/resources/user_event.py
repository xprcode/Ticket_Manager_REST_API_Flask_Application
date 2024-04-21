"""
UserEvent Resource

This module defines the UserEvent resource for retrieving user events.

"""
from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from rest_api_application.models.events import Events
from rest_api_application.models.eventparticipation import EventParticipation
from rest_api_application.models.user import User

class UserEvent(Resource):
    """
    UserEvent Resource Class

    Provides endpoints for retrieving user events.
    """
    @jwt_required()
    def get(self, user_id, event_id=None):
        """
        Retrieve user events.

        Args:
            user_id (int): The ID of the user.
            event_id (int, optional): The ID of the specific event (default is None).

        Returns:
            dict: A dictionary containing user events or a specific event if event_id is provided.
        """
        if not user_id:
            return {'error': 'User not found'}, 400

        user = User.query.filter(User.id == user_id).first()
        if not user:
            return {'error': 'User not found'}, 404

        if not event_id:
            participations = EventParticipation.query.filter_by(user_id=user_id).all()
            if not participations:
                return {'error': 'User has not any events added.'}, 400
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
