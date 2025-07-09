# ClubCommunity Flask REST API

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python app.py
   ```

The API will be available at `http://127.0.0.1:5000/`.

## Endpoints

### Clubs
- `POST   /clubs`         - Create a club
- `GET    /clubs`         - List all clubs
- `GET    /clubs/<id>`    - Get a club by ID
- `PUT    /clubs/<id>`    - Update a club
- `DELETE /clubs/<id>`    - Delete a club

### Events
- `POST   /events`         - Create an event
- `GET    /events`         - List all events
- `GET    /events/<id>`    - Get an event by ID
- `PUT    /events/<id>`    - Update an event
- `DELETE /events/<id>`    - Delete an event

### Users
- `POST   /users`         - Create a user
- `GET    /users`         - List all users
- `GET    /users/<id>`    - Get a user by ID
- `PUT    /users/<id>`    - Update a user
- `DELETE /users/<id>`    - Delete a user

### Sports
- `POST   /sports`         - Create a sport
- `GET    /sports`         - List all sports
- `GET    /sports/<id>`    - Get a sport by ID
- `PUT    /sports/<id>`    - Update a sport
- `DELETE /sports/<id>`    - Delete a sport 