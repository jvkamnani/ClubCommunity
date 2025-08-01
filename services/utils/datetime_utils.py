from datetime import datetime, timedelta

DATE_FORMAT = '%Y-%m-%d %H:%M'

def validate_date_format(date_str):
    """Check if the date string matches the format YYYY-MM-DD HH:mm."""
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except (ValueError, TypeError):
        return False


def is_at_least_two_days_after_today(date_str):
    """Check if the date is at least 2 days after today."""
    try:
        event_date = datetime.strptime(date_str, DATE_FORMAT)
        now = datetime.now()
        min_valid_date = now + timedelta(days=2)
        return event_date >= min_valid_date
    except (ValueError, TypeError):
        return False 