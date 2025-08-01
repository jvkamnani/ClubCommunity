def validate_required_fields(data, required_fields):
    """Check that all required fields are present and not None."""
    return [field for field in required_fields if field not in data or data[field] is None] 