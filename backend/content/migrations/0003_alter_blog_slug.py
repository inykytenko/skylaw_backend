# Generated by Django 4.0.6 on 2022-08-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_blog_image_blog_slug_alter_blog_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]
