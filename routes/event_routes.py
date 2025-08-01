from flask import Blueprint, request, jsonify, url_for
from services import *
from services.utils.datetime_utils import validate_date_format, is_at_least_two_days_after_today
from services.utils.field_utils import validate_required_fields
from models import Event

def model_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

event_bp = Blueprint('event_bp', __name__)

@event_bp.route('/events', methods=['POST'])
def create_event():
    data = request.json
    # Validation: all fields must be present and not null
    required_fields = ['name', 'date', 'club_id']
    missing_fields = validate_required_fields(data, required_fields)
    if missing_fields:
        return jsonify({'error': f"Missing or null fields: {', '.join(missing_fields)}"}), 400
    # Date format validation
    if not validate_date_format(data['date']):
        return jsonify({'error': 'Date must be in format YYYY-MM-DD HH:mm'}), 400
    # Date at least 2 days after today validation
    if not is_at_least_two_days_after_today(data['date']):
        return jsonify({'error': 'Date must be at least 2 days after today'}), 400
    event = create_event_service(name=data['name'], date=data['date'], club_id=data['club_id'])
    return jsonify(model_to_dict(event)), 201

@event_bp.route('/events', methods=['GET'])
def get_events():
    club_id = request.args.get('club_id')
    if club_id:
        events = get_events_by_club_service(club_id)
    else:
        events = get_events_service()
    return jsonify([model_to_dict(e) for e in events])


@event_bp.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = get_event_service(event_id)
    return jsonify(model_to_dict(event))

@event_bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    # Validation: all fields must be present and not null
    required_fields = ['name', 'date', 'club_id']
    missing_fields = validate_required_fields(data, required_fields)
    if missing_fields:
        return jsonify({'error': f"Missing or null fields: {', '.join(missing_fields)}"}), 400
    # Date format validation
    if not validate_date_format(data['date']):
        return jsonify({'error': 'Date must be in format YYYY-MM-DD HH:mm'}), 400
    # Date at least 2 days after today validation
    if not is_at_least_two_days_after_today(data['date']):
        return jsonify({'error': 'Date must be at least 2 days after today'}), 400
    event = update_event_service(event_id, name=data['name'], date=data['date'], club_id=data['club_id'])
    return jsonify(model_to_dict(event))

@event_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    delete_event_service(event_id)
    return '', 204 