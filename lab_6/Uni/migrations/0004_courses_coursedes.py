# Generated by Django 4.2.6 on 2023-10-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uni', '0003_alter_students_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='courseDes',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]