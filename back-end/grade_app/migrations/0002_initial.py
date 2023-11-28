# Generated by Django 4.2.7 on 2023-11-27 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grade_app', '0001_initial'),
        ('subject_app', '0001_initial'),
        ('student_app', '0005_student_subjects_alter_student_locker_combination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='a_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_app.subject'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.student'),
        ),
    ]
