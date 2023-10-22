from django.db import models
from django.core.validators import RegexValidator

class students(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField()
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
    student_id = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Student ID must be exactly 10 digits',
                code='invalid_student_id'
            )
        ]
    )

    def __str__(self):
        return f"{self.name},{self.email},{self.student_id},{self.phone_number}"
