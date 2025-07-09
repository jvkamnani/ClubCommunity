from flask import Flask, request, jsonify
from models import db, Club, Event, User, Sport
from services import *
from dotenv import load_dotenv
import os
from routes.user_routes import user_bp
from routes.club_routes import club_bp
from routes.event_routes import event_bp
from routes.sport_routes import sport_bp

app = Flask(__name__)
load_dotenv()

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_DB = os.getenv('MYSQL_DB', 'clubcommunity')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def model_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

app.register_blueprint(user_bp)
app.register_blueprint(club_bp)
app.register_blueprint(event_bp)
app.register_blueprint(sport_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 