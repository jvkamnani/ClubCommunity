from flask import Blueprint, request, jsonify, url_for
from services import *
from services.utils.field_utils import validate_required_fields
from models import Club
from models.form_template import FormTemplate

def model_to_dict(obj):
    data = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
    data['sport_ids'] = [sport.id for sport in obj.sports]
    return data

club_bp = Blueprint('club_bp', __name__)

@club_bp.route('/clubs', methods=['POST'])
def create_club():
    data = request.json
    required_fields = ['name']
    missing_fields = validate_required_fields(data, required_fields)
    if missing_fields:
        return jsonify({'error': f"Missing or null fields: {', '.join(missing_fields)}"}), 400
    club = create_club_service(name=data['name'], description=data.get('description'), sport_ids=data.get('sport_ids'))
    return jsonify(model_to_dict(club)), 201

@club_bp.route('/clubs', methods=['GET'])
def get_clubs():
    sport_id = request.args.get('sport_id')
    if sport_id:
        clubs = get_clubs_by_sport_service(sport_id)
    else:
        clubs = get_clubs_service()
    return jsonify([model_to_dict(c) for c in clubs])

@club_bp.route('/clubs/<uuid:club_id>', methods=['GET'])
def get_club(club_id):
    club = get_club_service(club_id)
    return jsonify(model_to_dict(club))

@club_bp.route('/clubs/<int:club_id>', methods=['PUT'])
def update_club(club_id):
    data = request.json
    required_fields = ['name']
    missing_fields = validate_required_fields(data, required_fields)
    if missing_fields:
        return jsonify({'error': f"Missing or null fields: {', '.join(missing_fields)}"}), 400
    club = update_club_service(club_id, name=data['name'], description=data.get('description'), sport_ids=data.get('sport_ids'))
    return jsonify(model_to_dict(club))

@club_bp.route('/clubs/<int:club_id>', methods=['DELETE'])
def delete_club(club_id):
    delete_club_service(club_id)
    return '', 204 