from flask import Blueprint, request, jsonify, send_file, url_for
from services import *
from models import Sport
import io

def model_to_dict(obj):
    data = {c.name: getattr(obj, c.name) for c in obj.__table__.columns if c.name != 'image'}
    if obj.image:
        data['image_url'] = url_for('sport_bp.get_sport_image', sport_id=obj.id, _external=True)
    else:
        data['image_url'] = None
    return data

sport_bp = Blueprint('sport_bp', __name__)

@sport_bp.route('/sports', methods=['POST'])
def create_sport():
    name = request.form.get('name')
    image = request.files.get('image')
    image_data = image.read() if image else None
    sport = create_sport_service(name=name, image=image_data)
    return jsonify(model_to_dict(sport)), 201

@sport_bp.route('/sports', methods=['GET'])
def get_sports():
    sports = get_sports_service()
    return jsonify([model_to_dict(s) for s in sports])

@sport_bp.route('/sports/<uuid:sport_id>', methods=['GET'])
def get_sport(sport_id):
    sport = get_sport_service(sport_id)
    return jsonify(model_to_dict(sport))

@sport_bp.route('/sports/<sport_id>/image', methods=['GET'])
def get_sport_image(sport_id):
    sport = get_sport_service(sport_id)
    if sport.image:
        return send_file(io.BytesIO(sport.image), mimetype='image/jpeg')
    return '', 404

@sport_bp.route('/sports/<uuid:sport_id>', methods=['PUT'])
def update_sport(sport_id):
    name = request.form.get('name')
    image = request.files.get('image')
    image_data = image.read() if image else None
    sport = update_sport_service(sport_id, name=name, image=image_data)
    return jsonify(model_to_dict(sport))

@sport_bp.route('/sports/<uuid:sport_id>', methods=['DELETE'])
def delete_sport(sport_id):
    delete_sport_service(sport_id)
    return '', 204 