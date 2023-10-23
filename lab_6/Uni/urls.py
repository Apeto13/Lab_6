from django.urls import path
from . import views

urlpatterns = [
    path('student', views.students, name="Students"),
    path('courses',views.Courses,name="Courses"),
    path('<int:student_id>',views.Details,name="Details")
]
