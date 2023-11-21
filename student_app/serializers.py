from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']

class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'personal_email', 'locker_number', 'locker_combination', 'good_student']



# {
#   "name": "John W. Watson",
#   "student_email": "thisIsAnEmail@school.com",
#   "personal_email": "thisIsAnEmail@gmail.com",
#   "locker_number": 13,
#   "locker_combination": "12-33-44",
#   "good_student": true
# }