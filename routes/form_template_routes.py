from flask import Blueprint, request, jsonify
from services.form_template_service import (
    create_form_template_with_fields,
    get_form_templates,
    get_form_template,
    update_form_template,
    delete_form_template
)
from services.utils.field_utils import validate_required_fields
from models import FormTemplate, FormField

def model_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

form_template_bp = Blueprint('form_template_bp', __name__)

@form_template_bp.route('/form_templates', methods=['POST'])
def create_form_template():
    data = request.json
    required_fields = ['name', 'club_id']
    missing = validate_required_fields(data, required_fields)
    if missing:
        return jsonify({'error': f"Missing or null fields: {', '.join(missing)}"}), 400
    template, created_fields = create_form_template_with_fields(
        name=data['name'],
        club_id=data['club_id'],
        description=data.get('description'),
        fields=data.get('fields', [])
    )
    return jsonify({
        **model_to_dict(template),
        'fields': [model_to_dict(f) for f in created_fields]
    }), 201

@form_template_bp.route('/form_templates', methods=['GET'])
def get_form_templates_route():
    templates = get_form_templates()
    return jsonify([
        model_to_dict(t) for t in templates
    ])

@form_template_bp.route('/form_templates/<uuid:template_id>', methods=['GET'])
def get_form_template_route(template_id):
    template = get_form_template(str(template_id))
    return jsonify(model_to_dict(template))

@form_template_bp.route('/form_templates/<uuid:template_id>', methods=['PUT'])
def update_form_template_route(template_id):
    data = request.json
    template = update_form_template(
        str(template_id),
        name=data.get('name'),
        description=data.get('description'),
        club_id=data.get('club_id')
    )
    return jsonify(model_to_dict(template))

@form_template_bp.route('/form_templates/<uuid:template_id>', methods=['DELETE'])
def delete_form_template_route(template_id):
    delete_form_template(str(template_id))
    return '', 204 