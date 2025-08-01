from models import db, FormTemplate, FormField
import uuid

# Create a form template and its fields
def create_form_template_with_fields(name, club_id, description=None, fields=None):
    template = FormTemplate(id=str(uuid.uuid4()), name=name, description=description, club_id=club_id)
    db.session.add(template)
    db.session.flush()  # Get template.id before commit
    created_fields = []
    if fields:
        for field in fields:
            form_field = FormField(
                id=str(uuid.uuid4()),
                template_id=template.id,
                label=field['label'],
                field_type=field['field_type'],
                is_required=field.get('is_required', False),
                options=field.get('options'),
                order=field.get('order'),
                validation=field.get('validation')
            )
            db.session.add(form_field)
            created_fields.append(form_field)
    db.session.commit()
    return template, created_fields

# Get all form templates
def get_form_templates():
    return FormTemplate.query.all()

# Get a form template by id
def get_form_template(template_id):
    return FormTemplate.query.get_or_404(template_id)

# Update a form template
def update_form_template(template_id, name=None, description=None, club_id=None):
    template = FormTemplate.query.get_or_404(template_id)
    if name is not None:
        template.name = name
    if description is not None:
        template.description = description
    if club_id is not None:
        template.club_id = club_id
    db.session.commit()
    return template

# Delete a form template
def delete_form_template(template_id):
    template = FormTemplate.query.get_or_404(template_id)
    db.session.delete(template)
    db.session.commit() 