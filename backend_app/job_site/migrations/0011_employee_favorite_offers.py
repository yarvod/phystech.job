# Generated by Django 3.2.9 on 2022-05-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_site', '0010_admin_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='favorite_offers',
            field=models.ManyToManyField(blank=True, related_name='employees_who_liked', to='job_site.Offer'),
        ),
    ]
