# Generated by Django 3.2.9 on 2022-03-21 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_site', '0002_auto_20220321_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='tag',
            new_name='tags',
        ),
    ]