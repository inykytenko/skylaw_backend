# Generated by Django 4.1 on 2022-09-08 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divorcements', '0009_divorcementchild'),
    ]

    operations = [
        migrations.RenameField(
            model_name='divorcementchild',
            old_name='birthday',
            new_name='child_birthday',
        ),
        migrations.RenameField(
            model_name='divorcementchild',
            old_name='name',
            new_name='child_full_name',
        ),
        migrations.RemoveField(
            model_name='divorcement',
            name='child_birthday',
        ),
        migrations.RemoveField(
            model_name='divorcement',
            name='child_full_name',
        ),
    ]
