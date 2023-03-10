# Generated by Django 4.1.5 on 2023-02-01 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ewp', '0004_initial'),
        ('courses', '0008_course_banner_course_institution_lecture_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.coursecontent'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ewp.university'),
        ),
    ]
