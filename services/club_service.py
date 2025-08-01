from models import db, Club, Sport

def create_club_service(name, description=None, sport_ids=None):
    club = Club(name=name, description=description)
    if sport_ids:
        club.sports = Sport.query.filter(Sport.id.in_(sport_ids)).all()
    db.session.add(club)
    db.session.commit()
    return club

def get_clubs_service():
    return Club.query.all()

def get_clubs_by_sport_service(sport_id):
    return Club.query.filter(Club.sports.any(Sport.id == sport_id)).all()

def get_club_service(club_id):
    return Club.query.get_or_404(club_id)

def update_club_service(club_id, name=None, description=None, sport_ids=None):
    club = Club.query.get_or_404(club_id)
    if name is not None:
        club.name = name
    if description is not None:
        club.description = description
    if sport_ids is not None:
        club.sports = Sport.query.filter(Sport.id.in_(sport_ids)).all()
    db.session.commit()
    return club

def delete_club_service(club_id):
    club = Club.query.get_or_404(club_id)
    db.session.delete(club)
    db.session.commit() 