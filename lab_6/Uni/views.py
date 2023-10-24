from django.shortcuts import render
from .models import students, courses

def index(request):
    All_students = students.objects.all()
    return render(request, "Uni/index.html",{
        "students": All_students
    })

def student(request, student_id):
    student = students.objects.get(id=student_id)
    return render(request, "Uni/student.html",{
        "student": student
    })

def course(request):
    pass

#def details(request):
#    student = students.object.get(id=students_id)
#    return render(request, "Uni/details.html",{
#        "student": student
#    })
