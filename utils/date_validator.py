from datetime import datetime


def validate_date(date_string):
    """
    Validates a date in DD-MM-YYYY format.

    Returns:
        True  -> Valid date
        False -> Invalid date
    """

    try:
        datetime.strptime(date_string, "%d-%m-%Y")
        return True
    except ValueError:
        return False