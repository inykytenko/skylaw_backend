# Generated by Django 4.1 on 2022-10-01 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divorcements', '0019_divorcement_court'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='divorcement',
            name='court_name',
        ),
    ]
