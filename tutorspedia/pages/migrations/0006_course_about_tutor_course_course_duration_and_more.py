# Generated by Django 4.1.1 on 2022-10-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about_tutor',
            field=models.TextField(default=0, max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='course_duration',
            field=models.TextField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='course_requirement',
            field=models.TextField(default=0, max_length=450),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='course_summary',
            field=models.TextField(default=0, max_length=450),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='tutor_portfoilo',
            field=models.TextField(default=0, max_length=35),
            preserve_default=False,
        ),
    ]