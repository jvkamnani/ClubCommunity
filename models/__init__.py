from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .club import Club
from .event import Event
from .user import User
from .sport import Sport
from .form_template import *
from .form_field import * 