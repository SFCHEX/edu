# Generated by Django 4.1.5 on 2023-01-30 12:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='date_added',
        ),
        migrations.AddField(
            model_name='attatchment',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.topic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]