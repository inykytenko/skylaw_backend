# Generated by Django 4.1 on 2022-08-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Divorcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_1', models.BooleanField(blank=True, null=True, verbose_name='Перший крок')),
                ('step_2', models.BooleanField(blank=True, null=True, verbose_name='Другий крок')),
                ('step_3', models.BooleanField(blank=True, null=True, verbose_name='Третій крок')),
                ('step_4', models.BooleanField(blank=True, null=True, verbose_name='Четвертий крок')),
                ('step_5', models.BooleanField(blank=True, null=True, verbose_name="П'ятий крок")),
                ('token', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]