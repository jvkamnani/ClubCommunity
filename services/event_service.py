from models import db, Event

def create_event_service(name, date=None, club_id=None):
    event = Event(name=name, date=date, club_id=club_id)
    db.session.add(event)
    db.session.commit()
    return event

def get_events_service():
    return Event.query.all()

def get_event_service(event_id):
    return Event.query.get_or_404(event_id)

def update_event_service(event_id, name=None, date=None, club_id=None):
    event = Event.query.get_or_404(event_id)
    if name is not None:
        event.name = name
    if date is not None:
        event.date = date
    if club_id is not None:
        event.club_id = club_id
    db.session.commit()
    return event

def delete_event_service(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit() 