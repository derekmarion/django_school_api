from django.urls import path
from .views import All_subjects, A_subject

urlpatterns = [
    path('', All_subjects.as_view(), name="all_subjects"),
    path('<str:subject>/', A_subject.as_view(), name='a_subject')
]