from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from rest_api_application import db
from rest_api_application.models.events import Events
from rest_api_application.models.eventparticipation import EventParticipation
from rest_api_application.models.user import User


class UserEvent(Resource):

    @jwt_required()
    def get(self, user_id, event_id=None):

        if event_id is None:
            # Query the EventParticipation table to get all event participation records for the user
            participations = EventParticipation.query.filter_by(user_id=user_id).all()

            # Extract the event IDs from the participation records
            event_ids = [participation.events_id for participation in participations]

            # Query the Event table to get all events associated with the event IDs
            
            events = Events.query.filter(Events.id.in_(event_ids)).all()
            all_event = [{
            'event_name': event.event_name,
            'event_adress': event.event_adress,
            'event_date': event.event_date
            } for event in events]
        

            if not event_id:
                return jsonify({'events': all_event})
            
        particular_event = EventParticipation.query.filter_by(user_id=user_id, events_id=event_id).first()

        if particular_event:
            event = Events.query.get(event_id)
            particular_event_2 = {
                'event_name': event.event_name,
                'event_adress': event.event_adress,
                'event_date': event.event_date
            }

        return jsonify({'event': particular_event_2})
        