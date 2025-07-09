from flask import Blueprint, request, jsonify
from services import *
from models import Club

def model_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

club_bp = Blueprint('club_bp', __name__)

@club_bp.route('/clubs', methods=['POST'])
def create_club():
    data = request.json
    club = create_club_service(name=data['name'], description=data.get('description'))
    return jsonify(model_to_dict(club)), 201

@club_bp.route('/clubs', methods=['GET'])
def get_clubs():
    clubs = get_clubs_service()
    return jsonify([model_to_dict(c) for c in clubs])

@club_bp.route('/clubs/<int:club_id>', methods=['GET'])
def get_club(club_id):
    club = get_club_service(club_id)
    return jsonify(model_to_dict(club))

@club_bp.route('/clubs/<int:club_id>', methods=['PUT'])
def update_club(club_id):
    data = request.json
    club = update_club_service(club_id, name=data.get('name'), description=data.get('description'))
    return jsonify(model_to_dict(club))

@club_bp.route('/clubs/<int:club_id>', methods=['DELETE'])
def delete_club(club_id):
    delete_club_service(club_id)
    return '', 204 