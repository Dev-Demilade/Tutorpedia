# Generated by Django 4.1.1 on 2022-10-17 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_course_about_tutor_course_course_duration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='about_tutor',
        ),
        migrations.RemoveField(
            model_name='course',
            name='tutor_image',
        ),
        migrations.RemoveField(
            model_name='course',
            name='tutor_name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='tutor_portfoilo',
        ),
    ]
