# Generated by Django 4.2.7 on 2023-11-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_student_good_student_student_locker_combination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
