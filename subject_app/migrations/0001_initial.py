# Generated by Django 4.2.7 on 2023-11-27 17:20

from django.db import migrations, models
import subject_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_app', '0004_alter_student_locker_combination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(default=None, unique=True, validators=[subject_app.validators.validate_subject_format])),
                ('professor', models.CharField(default='Mr. Cahan', validators=[subject_app.validators.validate_professor_name])),
                ('students', models.ManyToManyField(default=None, to='student_app.student')),
            ],
        ),
    ]