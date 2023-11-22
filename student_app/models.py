from django.db import models
from django.core import validators as v
from .validators import validate_name_format, validate_school_email, validate_combination_format, validate_subjects, validate_subject_format


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
    subjects = models.ManyToManyField(Subject, unique=False, default=None, validators=[validate_subjects], related_name='students')

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

    def add_subject(self, subject_id):
        new_subject = validate_subjects(self.subjects)
        if new_subject:
            self.subjects.append(subject_id)
    
    def remove_subject(self, subject_id):
        subject_to_remove = validate_subjects(self.subjects)
        if subject_to_remove:
            self.subjects.remove(subject_id)


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject_name = models.CharField(unique=True, default=None, null=False, validators=[validate_subject_format])
    professor = models.CharField(unique=False, null=False, default="Mr. Cahan", validators=[validate_professor_name])
    students = models.ManyToManyField(Student, unique=False, null=False, default=None, validators=[validate_class_capacity])

