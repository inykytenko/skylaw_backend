# Generated by Django 4.1 on 2022-08-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divorcements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divorcement',
            name='token',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
