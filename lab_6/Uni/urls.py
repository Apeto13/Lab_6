from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:student_id>', views.student, name="student"),
    # path('courses',views.courses,name="Courses"),
]
