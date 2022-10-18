# Generated by Django 4.1 on 2022-08-14 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_date', models.DateField(auto_now_add=True, null=True)),
                ('is_paid', models.BooleanField()),
                ('token', models.CharField(blank=True, max_length=16, null=True, verbose_name='токен')),
            ],
            options={
                'verbose_name': 'токен',
                'verbose_name_plural': 'токени',
            },
        ),
    ]