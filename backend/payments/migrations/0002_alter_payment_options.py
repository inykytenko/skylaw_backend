# Generated by Django 4.1 on 2022-08-14 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'оплата', 'verbose_name_plural': 'оплати'},
        ),
    ]