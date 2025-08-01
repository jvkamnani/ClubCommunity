from . import db
import uuid
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.types import String

club_sport = db.Table(
    'club_sport',
    db.Column('club_id', CHAR(36), db.ForeignKey('club.id'), primary_key=True),
    db.Column('sport_id', CHAR(36), db.ForeignKey('sport.id'), primary_key=True)
)

class Club(db.Model):
    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    sports = db.relationship('Sport', secondary=club_sport, backref=db.backref('clubs', lazy='dynamic')) 