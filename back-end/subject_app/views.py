from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class All_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.order_by("id"), many=True)
        return Response(subjects.data)


class A_subject(APIView):
    def get(self, request, subject):
        subject = get_object_or_404(Subject, subject_name=subject.title())
        return Response(SubjectSerializer(subject).data)
