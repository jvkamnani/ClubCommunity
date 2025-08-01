from . import db

class FormTemplate(db.Model):
    __tablename__ = 'form_template'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    club_id = db.Column(db.String(36), db.ForeignKey('club.id'), nullable=False)
    club = db.relationship('Club', backref=db.backref('form_templates', lazy=True))
    fields = db.relationship('FormField', backref='template', cascade='all, delete-orphan') 