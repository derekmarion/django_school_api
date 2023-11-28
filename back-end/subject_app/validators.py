from django.core.exceptions import ValidationError
import re


def validate_subject_format(subject_name):
    errorMessage = 'Subject must be in title case format.'
    if subject_name.istitle():
        return subject_name
    else:
        raise ValidationError(errorMessage)


def validate_professor_name(professor):
    errorMessage = 'Professor name must be in the format "Professor Adam".'
    regex = re.compile(r"^Professor \w+$")
    if regex.fullmatch(professor):
        return professor
    else:
        raise ValidationError(errorMessage, params={"professor": professor})