from django.core.exceptions import ValidationError
import re


def validate_subjects(subjects):
    errorMessageFull = "This students class schedule is full!"
    errorMessageEmpty = "This students class schedule is empty!"
    if 0 < len(subjects) < 8:
        return subjects
    elif len(subjects) > 8:
        raise ValidationError(errorMessageFull, params={"subjects": subjects})
    elif len(subjects) < 1:
        raise ValidationError(errorMessageEmpty, params={"subjects": subjects})


def validate_subject_format(subject_name):
    errorMessage = "Subject must be in the title case format"
    if subject_name.istitle():
        return subject_name
    else:
        raise ValidationError(errorMessage, params={"subject_name": subject_name})


def validate_professor_name(professor):
    errorMessage = 'Professor name must be in the format "Professor Adam".'
    regex = re.compile(r"^Professor \w+$")
    if regex.fullmatch(professor):
        return professor
    else:
        raise ValidationError(errorMessage, params={"professor": professor})
    

def validate_class_capacity(students, drop=None):
    errorMessageFull = "This subject is full!"
    errorMessageEmpty = "This subject is empty!"

    student_list = list(students.all())  #Must convert to list since you can't check length of ManyRelatedManager object

    if 0 < len(student_list) < 31:
        return students
    elif len(student_list) < 1 and drop:
        raise ValidationError(errorMessageEmpty, params={"students": students})
    elif len(student_list) > 30:
        raise ValidationError(errorMessageFull, params={"students": students})