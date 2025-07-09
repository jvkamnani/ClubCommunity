from models import db, User

def create_user_service(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user

def get_users_service():
    return User.query.all()

def get_user_service(user_id):
    return User.query.get_or_404(user_id)

def update_user_service(user_id, username=None, email=None):
    user = User.query.get_or_404(user_id)
    if username is not None:
        user.username = username
    if email is not None:
        user.email = email
    db.session.commit()
    return user

def delete_user_service(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit() 