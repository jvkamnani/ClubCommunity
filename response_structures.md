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
## 6. Register for an event
### Endpoint:
`POST /events/{eventId}/register`
### Description:
Register the authenticated user for a specific event. Returns different responses based on event type (free vs paid).
### Sample Response (Free Event):
```json
{
  "registration_id": "550e8400-e29b-41d4-a716-446655440000",
  "event_id": "550e8400-e29b-41d4-a716-446655440001",
  "status": "confirmed",
  "registration_date": "2025-06-19T10:30:00Z",
  "participant_details": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```
### Sample Response (Paid Event):
```json
{
  "registration_id": "550e8400-e29b-41d4-a716-446655440002",
  "event_id": "550e8400-e29b-41d4-a716-446655440001",
  "status": "pending_payment",
  "payment_required": true,
  "amount": 25.00,
  "currency": "USD",
  "payment_deadline": "2025-06-26T23:59:59Z"
}
```

## 7. Join event waitlist
### Endpoint:
`POST /events/{eventId}/register/waitlist`
### Description:
Join the waitlist for a full event when no spots are available.
### Sample Response:
```json
{
  "waitlist_id": "550e8400-e29b-41d4-a716-446655440003",
  "event_id": "550e8400-e29b-41d4-a716-446655440001",
  "position": 5,
  "estimated_notification_date": "2025-06-25T00:00:00Z",
  "status": "active"
}
```

## 8. Check event availability
### Endpoint:
`GET /events/{eventId}/register/availability`
### Description:
Check if event has available spots or waitlist information before attempting registration.
### Sample Response:
```json
{
  "event_id": "550e8400-e29b-41d4-a716-446655440001",
  "available_spots": 15,
  "max_capacity": 100,
  "waitlist_available": true,
  "waitlist_count": 8,
  "registration_status": "open"
}
```

## 9. Get registration details
### Endpoint:
`GET /registrations/{registrationId}`
### Description:
Get detailed information about a specific registration including status and participant details.
### Sample Response:
```json
{
  "registration_id": "550e8400-e29b-41d4-a716-446655440000",
  "event_id": "550e8400-e29b-41d4-a716-446655440001",
  "event_name": "Annual Marathon Training",
  "participant_id": "550e8400-e29b-41d4-a716-446655440004",
  "status": "confirmed",
  "registration_date": "2025-06-19T10:30:00Z",
  "payment_status": "completed",
  "check_in_status": "not_checked_in",
  "participant_details": {
    "name": "Jane Smith",
    "email": "jane@example.com",
    "phone": "+1-555-0123"
  }
}
```

## 10. Update registration
### Endpoint:
`PATCH /registrations/{registrationId}`
### Description:
Update registration details such as participant information before the event starts.
### Sample Response:
```json
{
  "registration_id": "550e8400-e29b-41d4-a716-446655440000",
  "event_id": "550e8400-e29b-41d4-a716-446655440001",
  "status": "confirmed",
  "last_updated": "2025-06-19T14:15:00Z",
  "participant_details": {
    "name": "Jane Smith-Johnson",
    "email": "jane.johnson@example.com",
    "phone": "+1-555-0456"
  }
}
```

## 11. Cancel registration
### Endpoint:
`DELETE /registrations/{registrationId}`
### Description:
Cancel a registration subject to the event's cancellation policy.
### Sample Response:
```json
{
  "registration_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "cancelled",
  "cancellation_date": "2025-06-19T16:45:00Z",
  "refund_amount": 20.00,
  "refund_status": "processing",
  "reason": "Schedule conflict"
}
```

## 12. Process payment for registration
### Endpoint:
`POST /registrations/{registrationId}/payment`
### Description:
Complete payment for a pending registration to confirm the booking.
### Sample Response:
```json
{
  "registration_id": "550e8400-e29b-41d4-a716-446655440002",
  "payment_id": "pay_550e8400e29b41d4a716446655440005",
  "status": "completed",
  "amount": 25.00,
  "currency": "USD",
  "payment_method": "card_ending_4242",
  "transaction_date": "2025-06-19T11:20:00Z",
  "registration_status": "confirmed"
}
```


## Notes:

* UUIDs are used for `id` fields to ensure global uniqueness.
* Dates are returned in `YYYY-MM-DD` ISO 8601 format.
* All image fields are absolute URLs pointing to static resources.

Let me know if you'd like to include error response templates or add `POST`, `PUT`, `DELETE` examples.
