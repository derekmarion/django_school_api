from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentAllSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class All_students(APIView):
    def get(self, request):
        students = StudentAllSerializer(Student.object.order_by("id"), many=True)
        return Response(students.data)
