from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('course', views.course, name="course"),
    path('<int:student_id>', views.student, name="student"),
    path('<int:student_id>/add_course', views.add_course, name="add_course"),
]
