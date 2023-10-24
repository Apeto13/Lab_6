from django.db import models
from django.core.validators import RegexValidator

class students(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=64)
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be exactly 10 digits',
                code='invalid_phone_number'
            )
        ]
    )
    student_ID = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Student ID must be exactly 10 digits',
                code='invalid_student_ID'
            )
        ]
    )
    courses = models.ManyToManyField('courses', blank=True, related_name="students") 

    def __str__(self):
        return f"{self.name},{self.email},{self.student_ID},{self.phone_number},{self.courses}"

class courses(models.Model):
    coursesid = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.coursesid}"