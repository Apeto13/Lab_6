# Generated by Django 4.2.6 on 2023-10-23 23:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursesid', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must be exactly 10 digits', regex='^\\d{10}$')])),
                ('student_id', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_student_id', message='Student ID must be exactly 10 digits', regex='^\\d{10}$')])),
                ('courses', models.ManyToManyField(blank=True, related_name='students', to='Uni.courses')),
            ],
        ),
    ]
