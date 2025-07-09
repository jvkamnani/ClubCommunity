from models import db, Sport

def create_sport_service(name, image=None):
    sport = Sport(name=name, image=image)
    db.session.add(sport)
    db.session.commit()
    return sport

def get_sports_service():
    return Sport.query.all()

def get_sport_service(sport_id):
    return Sport.query.get_or_404(sport_id)

def update_sport_service(sport_id, name=None, image=None):
    sport = Sport.query.get_or_404(sport_id)
    if name is not None:
        sport.name = name
    if image is not None:
        sport.image = image
    db.session.commit()
    return sport

def delete_sport_service(sport_id):
    sport = Sport.query.get_or_404(sport_id)
    db.session.delete(sport)
    db.session.commit() 