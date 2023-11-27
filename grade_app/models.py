from django.db import models
from django.core import validators as v


# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(
        default=100,
        blank=False,
        unique=False,
        decimal_places=2,
        max_digits=5,
        validators=[v.MinValueValidator(0.00), v.MaxValueValidator(100.00)],
    )
    a_subject = models.ForeignKey("subject_app.Subject", on_delete=models.CASCADE)
    student = models.ForeignKey("student_app.Student", on_delete=models.CASCADE)
