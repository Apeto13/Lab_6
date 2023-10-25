from django.contrib import admin
from .models import students, courses


class StudentAdmin(admin.ModelAdmin):
    list_display=("id","name","email","phone_number","student_ID")

class CoursesAdmin(admin.ModelAdmin):
    list_display=("id","coursesid","courseDes")



admin.site.register(students, StudentAdmin)
admin.site.register(courses, CoursesAdmin)