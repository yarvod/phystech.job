# Generated by Django 3.2.9 on 2022-04-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_site', '0006_auto_20220407_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='favorite_vacancies',
            field=models.ManyToManyField(blank=True, related_name='employees_who_liked', to='job_site.Vacancy'),
        ),
    ]