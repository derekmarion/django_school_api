from django.core.exceptions import ValidationError
import re


def validate_name_format(name):
    regex = re.compile(r"^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$")
    errorMessage = (
        "Validation Error: 'Name must be in the format 'First Middle Initial. Last'"
    )
    if regex.fullmatch(name):
        return name
    else:
        raise ValidationError(errorMessage, params={"name": name})


def validate_school_email(email):
    regex = re.compile(r'^[a-zA-Z0-9._%+-]+@school\.com$')
    errorMessage = "Validation Error: 'Invalid school email format. Please use an email ending with '@school.com'"
    if regex.fullmatch(email):
        return email
    else:
        raise ValidationError(errorMessage, params={"email": email})


def validate_combination_format(combo):
    regex = re.compile(r'^\d{2}-\d{2}-\d{2}$')
    errorMessage = "Validation Error: 'Combination must be in the format '12-12-12'"
    if regex.fullmatch(combo):
        return combo
    else:
        raise ValidationError(errorMessage, params={"combo": combo})
