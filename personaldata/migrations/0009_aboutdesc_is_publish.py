# Generated by Django 3.2.6 on 2021-08-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaldata', '0008_aboutdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutdesc',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]
