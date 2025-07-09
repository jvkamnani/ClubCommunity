from models import db, Club

def create_club_service(name, description=None):
    club = Club(name=name, description=description)
    db.session.add(club)
    db.session.commit()
    return club

def get_clubs_service():
    return Club.query.all()

def get_club_service(club_id):
    return Club.query.get_or_404(club_id)

def update_club_service(club_id, name=None, description=None):
    club = Club.query.get_or_404(club_id)
    if name is not None:
        club.name = name
    if description is not None:
        club.description = description
    db.session.commit()
    return club

def delete_club_service(club_id):
    club = Club.query.get_or_404(club_id)
    db.session.delete(club)
    db.session.commit() 