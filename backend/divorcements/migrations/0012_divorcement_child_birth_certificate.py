# Generated by Django 4.1 on 2022-09-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divorcements', '0011_remove_divorcement_child_birth_certificate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='divorcement',
            name='child_birth_certificate',
            field=models.FileField(blank=True, null=True, upload_to='images', verbose_name='Фото свідотцва про народження дитини'),
        ),
    ]
