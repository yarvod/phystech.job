# Generated by Django 3.2.9 on 2022-05-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='as_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='as_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='as_employer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='as_freelancer',
            field=models.BooleanField(default=False),
        ),
    ]
