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

# Clubs API

## Create a Club with Multiple Sports

To create a club associated with one or more sports, provide a list of sport UUIDs in the `sport_ids` field:

```
POST /clubs
Content-Type: application/json

{
  "name": "Chess Club",
  "description": "A club for chess lovers",
  "sport_ids": ["uuid-sport-1", "uuid-sport-2"]
}
```

## Update a Club's Sports

To update the sports associated with a club, send a list of sport UUIDs in the `sport_ids` field:

```
PUT /clubs/<club_id>
Content-Type: application/json

{
  "sport_ids": ["uuid-sport-1", "uuid-sport-3"]
}
```

## Club Response Example

A club object will include a `sport_ids` field listing all associated sports:

```
{
  "id": "...",
  "name": "...",
  "description": "...",
  "sport_ids": ["uuid-sport-1", "uuid-sport-2"]
}
```

## Get Clubs by Sport ID

Fetch all clubs for a specific sport:

```
GET /clubs?sport_id=<sport_id>
```

**Query Parameters:**
- `sport_id` (string, required): The UUID of the sport to filter clubs by.

**Response:**
- 200 OK: List of club objects for the specified sport.

Example:
```
GET /clubs?sport_id=123e4567-e89b-12d3-a456-426614174000
```

Returns:
```
[
  {
    "id": "...",
    "name": "...",
    "description": "...",
    "sport_ids": ["..."]
  },
  ...
]
```

---

# Events API

## Get Events by Club ID

Fetch all events for a specific club:

```
GET /events?club_id=<club_id>
```

**Query Parameters:**
- `club_id` (string, required): The UUID of the club to filter events by.

**Response:**
- 200 OK: List of event objects for the specified club.

Example:
```
GET /events?club_id=123e4567-e89b-12d3-a456-426614174000
```

Returns:
```
[
  {
    "id": "...",
    "name": "...",
    "date": "...",
    "club_id": "..."
  },
  ...
]
```

--- 