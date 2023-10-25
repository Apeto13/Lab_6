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

def add_course(request, student_id):
    if request.method == "POST":
        student = students.objects.get(pk=student_id)
        course_id = int(request.POST["course"])
        course = courses.objects.get(pk=course_id)
        student.courses.add(course)
        return HttpResponseRedirect(reverse("student",args=(student.id,)))
    

def create_course(request):
    if request.method == "POST":
        courseName = request.POST.get("coursesid","")
        course_Des = request.POST.get("courseDes","")
        new_course = courses(coursesid=courseName,courseDes=course_Des)
        new_course.save()
        return HttpResponseRedirect(reverse("course"))

def view_student(request):
    return render(request,"Uni/index.html",)

def create_student(request):
    if request.method =="POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone_num = request.POST.get("phone_number","")
        id = request.POST.get("student_ID","")
        new_student = students(name=name,email=email,phone_number=phone_num,student_ID=id)
        new_student.save()
        return HttpResponseRedirect(reverse('index'))
        # HttpResponseRedirect(reverse("signin:index"))