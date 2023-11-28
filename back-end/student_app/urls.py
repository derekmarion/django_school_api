from django.urls import path
from .views import All_students, A_student

urlpatterns = [
    path('', All_students.as_view(), name="all_students"),
    path('<int:id>/', A_student.as_view(), name='a_student')
]