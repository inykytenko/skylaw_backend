# Generated by Django 4.1 on 2022-09-01 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divorcements', '0006_remove_divorcement_city_divorcement_court_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='divorcement',
            options={'verbose_name': 'Розлучення', 'verbose_name_plural': 'Розлучення'},
        ),
    ]
