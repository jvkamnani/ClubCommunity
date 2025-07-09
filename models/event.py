from . import db
import uuid
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.types import String

class Event(db.Model):
    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(20))
    club_id = db.Column(CHAR(36), db.ForeignKey('club.id'))
    club = db.relationship('Club', backref=db.backref('events', lazy=True)) 