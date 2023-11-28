from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()
    
    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'students', 'grade_average']

    def get_students(self, obj):
        return obj.students.count()
    
    def get_grade_average(self, obj):
        grades = obj.grades.all()
        return round(sum([x.grade for x in grades])/len(grades), 2)