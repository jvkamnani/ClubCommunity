from flask import Blueprint, request, jsonify
from services import *
from services.utils.field_utils import validate_required_fields
from models import User

def model_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    required_fields = ['username', 'email']
    missing_fields = validate_required_fields(data, required_fields)
    if missing_fields:
        return jsonify({'error': f"Missing or null fields: {', '.join(missing_fields)}"}), 400
    user = create_user_service(username=data['username'], email=data['email'])
    return jsonify(model_to_dict(user)), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_users_service()
    return jsonify([model_to_dict(u) for u in users])

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_service(user_id)
    return jsonify(model_to_dict(user))

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    required_fields = ['username', 'email']
    missing_fields = validate_required_fields(data, required_fields)
    if missing_fields:
        return jsonify({'error': f"Missing or null fields: {', '.join(missing_fields)}"}), 400
    user = update_user_service(user_id, username=data['username'], email=data['email'])
    return jsonify(model_to_dict(user))

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    delete_user_service(user_id)
    return '', 204 