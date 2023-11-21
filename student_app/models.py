from django.db import models
from django.core import validators as v
from .validators import validate_name_format, validate_school_email, validate_combination_format


# Create your models here.
class Student(models.Model):
    name = models.CharField(default="name", validators=[validate_name_format])
    student_email = models.EmailField(
        default="student@school.com", unique=True, validators=[validate_school_email]
    )
    personal_email = models.EmailField(blank=True, unique=True)
    locker_number = models.IntegerField(
        default=110,
        unique=True,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
    )
    locker_combination = models.CharField(default="12-12-12", unique=False, validators=[validate_combination_format])
    good_student = models.BooleanField(default=True, unique=False)

    def __str__(self) -> str:
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    @property
    def get_locker_number(self):
        return self.locker_number

    @get_locker_number.setter
    def update_locker_number(self, new_locker):
        self.locker_number = new_locker
        self.save()

    @property
    def get_good_sudent(self):
        return self.good_student

    @get_good_sudent.setter
    def update_good_student(self, new_status):
        self.good_student = new_status
        self.save()
