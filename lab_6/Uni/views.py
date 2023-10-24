from django.shortcuts import render
from .models import students, courses
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    All_students = students.objects.all()
    return render(request, "Uni/index.html",{
        "students": All_students
    })

def student(request, student_id):
    student = students.objects.get(id=student_id)
    All_courses = student.courses.all()
    Noncourses = courses.objects.exclude(students=student).all() 
    return render(request, "Uni/student.html",{
        "student": student,
        "courses": All_courses,
        "Noncourses": Noncourses
    })

def course(request):
    All_courses = courses.objects.all()
    return render(request, "Uni/course.html",{
        "courses": All_courses
    })

def add_course(request, course_id):
    if request.method == "POST":
        course = courses.objects.get(pk=course_id)
        student_id = int(request.POST["student"])
        student = students.objects.get(pk=student_id)
        student.courses.add(student)
        return HttpResponseRedirect(reverse("course",args=(course.id,)))
        

    

#def details(request):
#    student = students.object.get(id=students_id)
#    return render(request, "Uni/details.html",{
#        "student": student
#    })
