from django.db import models
from .validators import (
    validate_subject_format,
    validate_professor_name,
)


# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(
        unique=True, default=None, null=False, validators=[validate_subject_format]
    )
    professor = models.CharField(
        unique=False,
        null=False,
        default="Mr. Cahan",
        validators=[validate_professor_name],
    )
    # related field students mtm field from Student model

    def __str__(self) -> str:
        return f"{self.subject_name}-{self.professor}-{self.students.count()}"

    def add_a_student(self, student_id):
        if self.students.count() < 31:
            self.students.add(student_id)
        else:
            raise Exception("This subject is full!")

    def drop_a_student(self, student_id):
        if self.students.count() > 0:
            self.students.remove(student_id)
        else:
            raise Exception("This subject is empty!")