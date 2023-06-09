# Generated by Django 4.0.4 on 2023-05-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_is_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=[True, 'Your email is already exist'], verbose_name='email address'),
        ),
    ]
