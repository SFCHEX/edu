# Generated by Django 4.1.5 on 2023-01-30 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_attatchment_lecture_remove_attatchment_topic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecontent',
            name='Name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
