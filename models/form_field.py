from . import db

class FormField(db.Model):
    __tablename__ = 'form_field'
    id = db.Column(db.String(36), primary_key=True)
    template_id = db.Column(db.String(36), db.ForeignKey('form_template.id'), nullable=False)
    label = db.Column(db.String, nullable=False)
    field_type = db.Column(db.String, nullable=False)
    is_required = db.Column(db.Boolean, nullable=False, default=False)
    options = db.Column(db.Text)
    order = db.Column(db.Integer)
    validation = db.Column(db.Text) 