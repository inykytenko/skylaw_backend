# Generated by Django 4.0.6 on 2022-08-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to='images'),
        ),
    ]