from django.urls import path
from .views import All_students

urlpatterns = [
    path('', All_students.as_view(), name="all_students")
]