from django.shortcuts import render

# Create your views here.
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class All_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.order_by("id"), many=True)
        return Response(subjects.data)
