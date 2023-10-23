from django.contrib import admin
from .models import students, courses

admin.site.register(students)
admin.site.register(courses)