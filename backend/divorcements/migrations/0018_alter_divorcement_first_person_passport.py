# Generated by Django 4.1 on 2022-09-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divorcements', '0017_alter_divorcement_first_person_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divorcement',
            name='first_person_passport',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Фото паспорта'),
        ),
    ]
