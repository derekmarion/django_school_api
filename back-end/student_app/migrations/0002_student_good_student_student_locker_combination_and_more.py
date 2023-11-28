# Generated by Django 4.2.7 on 2023-11-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='good_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='locker_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='name'),
        ),
        migrations.AddField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(default='student@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.EmailField(default='student@school.com', max_length=254),
        ),
    ]