from . import db
import uuid
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.types import String

class User(db.Model):
    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) 