# Generated by Django 4.2.6 on 2023-10-24 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Uni', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='student_id',
            new_name='student_ID',
        ),
    ]