from django.db import models
from .validators import (
    validate_subject_format,
    validate_professor_name,
    validate_class_capacity,
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
    students = models.ManyToManyField(
        'student_app.Student', unique=False, default=None, related_name='subjects'
    )

    def __str__(self) -> str:
        return f"{self.subject_name}-{self.professor}-{len(self.students)}"

    def add_a_student(self, student_id):
        if validate_class_capacity:
            self.students.add(student_id)

    def drop_a_student(self, student_id):
        if validate_class_capacity:
            self.students.remove(student_id)
