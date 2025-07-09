from . import db
import uuid
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.types import String

class Club(db.Model):
    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200)) 