import re


def validate_name(name):
    return len(name.strip()) > 0


def validate_course(course):
    return len(course.strip()) > 0


def validate_duration(duration):
    return len(duration.strip()) > 0


def validate_level(level):
    return len(level.strip()) > 0


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10