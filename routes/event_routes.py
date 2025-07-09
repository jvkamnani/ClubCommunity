from flask import Blueprint, request, jsonify
from services import *
from models import Event

def model_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

event_bp = Blueprint('event_bp', __name__)

@event_bp.route('/events', methods=['POST'])
def create_event():
    data = request.json
    event = create_event_service(name=data['name'], date=data.get('date'), club_id=data.get('club_id'))
    return jsonify(model_to_dict(event)), 201

@event_bp.route('/events', methods=['GET'])
def get_events():
    events = get_events_service()
    return jsonify([model_to_dict(e) for e in events])

@event_bp.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = get_event_service(event_id)
    return jsonify(model_to_dict(event))

@event_bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    event = update_event_service(event_id, name=data.get('name'), date=data.get('date'), club_id=data.get('club_id'))
    return jsonify(model_to_dict(event))

@event_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    delete_event_service(event_id)
    return '', 204 