# Generated by Django 4.1.5 on 2023-01-30 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_coursecontent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='attachments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lecture'),
        ),
    ]