from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create_student',views.create_student,name="create_student"),
    path('course', views.course, name="course"),
    path('course/create_course', views.create_course, name="create_course"),
    path('<int:student_id>', views.student, name="student"),
    path('<int:student_id>/add_course>', views.add_course, name="add_course"),
]
