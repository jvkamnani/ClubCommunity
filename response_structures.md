# API Response Templates and Documentation

This document outlines the structure of API responses for key endpoints in the system including sports, clubs, and events.

---

## 1. Sports API

### Endpoint:

`GET /api/sports`

### Description:

Fetches the list of all sports available in the system.

### Sample Response:

```json
[
  {
    "id": "b7f9a92c-3215-431f-bd7c-91c7a3b8e93a",
    "name": "Running",
    "image": "https://example.com/static/images/running.png"
  },
  {
    "id": "c14ecbc4-9e4c-4264-9bbf-4a4c54ad0f2a",
    "name": "Football",
    "image": "https://example.com/static/images/football.png"
  }
]
```

---

## 2. Clubs API

### Endpoint:

`GET /api/clubs`

### Description:

Fetches a list of all clubs, including basic metadata and their sport associations.

### Sample Response:

```json
[
  {
    "id": "9d2e5c21-d5ef-498c-8932-fc2e3f1b2c61",
    "name": "Speed Demons",
    "description": "A club for intermediate to advanced runners.",
    "area": "Indiranagar",
    "beginner_friendly": true,
    "sport": {
      "id": "b7f9a92c-3215-431f-bd7c-91c7a3b8e93a",
      "name": "Running",
      "image": "https://example.com/static/images/running.png"
    }
  }
]
```

---

## 3. Clubs Based on Sport API

### Endpoint:

`GET /api/sports/<sport_id>/clubs`

### Description:

Fetches clubs filtered by a specific sport.

### Sample Response:

```json
[
  {
    "id": "9d2e5c21-d5ef-498c-8932-fc2e3f1b2c61",
    "name": "Speed Demons",
    "description": "A club for intermediate to advanced runners.",
    "area": "Indiranagar",
    "beginner_friendly": true,
    "sport_id": "b7f9a92c-3215-431f-bd7c-91c7a3b8e93a"
  }
]
```

---

## 4. Events API

### Endpoint:

`GET /api/events`

### Description:

Returns a list of all events regardless of their club association.

### Sample Response:

```json
[
  {
    "id": 1,
    "name": "Sunday Long Run",
    "event_date": "2025-07-01",
    "location": "Cubbon Park",
    "cost": 0,
    "max_capacity": 50,
    "registered_count": 22,
    "club_id": "9d2e5c21-d5ef-498c-8932-fc2e3f1b2c61"
  }
]
```

---

## 5. Events Based on Club API

### Endpoint:

`GET /api/clubs/<club_id>/events`

### Description:

Fetches events specific to a given club.

### Sample Response:

```json
[
  {
    "id": 1,
    "name": "Sunday Long Run",
    "event_date": "2025-07-01",
    "location": "Cubbon Park",
    "cost": 0,
    "max_capacity": 50,
    "registered_count": 22
  }
]
```

---

## Notes:

* UUIDs are used for `id` fields to ensure global uniqueness.
* Dates are returned in `YYYY-MM-DD` ISO 8601 format.
* All image fields are absolute URLs pointing to static resources.

Let me know if you'd like to include error response templates or add `POST`, `PUT`, `DELETE` examples.
