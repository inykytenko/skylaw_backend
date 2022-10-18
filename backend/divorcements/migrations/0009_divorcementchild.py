# Generated by Django 4.1 on 2022-09-07 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divorcements', '0008_rename_first_person_telefon_number_divorcement_first_person_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DivorcementChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ПІБ дитини')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='День народження дитини')),
                ('divorcement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='divorcements.divorcement')),
            ],
            options={
                'verbose_name': 'Дитина',
                'verbose_name_plural': 'Діти',
            },
        ),
    ]
