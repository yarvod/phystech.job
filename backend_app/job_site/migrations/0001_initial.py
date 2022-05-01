# Generated by Django 3.2.9 on 2022-04-29 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='job_site.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True, null=True)),
                ('duties', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('conditions', models.TextField(blank=True, null=True)),
                ('salary_min', models.PositiveIntegerField(blank=True, null=True)),
                ('salary_max', models.PositiveIntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('distant_work', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vacancies', to='job_site.category')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='job_site.employer')),
                ('tags', models.ManyToManyField(blank=True, related_name='vacancies', to='job_site.Tag')),
            ],
            options={
                'verbose_name_plural': 'Vacancies',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True, null=True)),
                ('salary', models.PositiveIntegerField()),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='job_site.category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='job_site.client')),
                ('tags', models.ManyToManyField(blank=True, related_name='tasks', to='job_site.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True, null=True)),
                ('salary', models.PositiveIntegerField()),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='services', to='job_site.category')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='services', to='job_site.freelancer')),
                ('tags', models.ManyToManyField(blank=True, related_name='services', to='job_site.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('work_experiance', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('ready_relocate', models.BooleanField(default=False)),
                ('ready_distant_work', models.BooleanField(default=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resumes', to='job_site.category')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='job_site.employee')),
                ('tags', models.ManyToManyField(blank=True, related_name='resumes', to='job_site.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='freelancer',
            name='favorite_tasks',
            field=models.ManyToManyField(blank=True, related_name='freelancers_who_liked', to='job_site.Task'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employer',
            name='favorite_resumes',
            field=models.ManyToManyField(blank=True, related_name='employers_who_liked', to='job_site.Resume'),
        ),
        migrations.AddField(
            model_name='employer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='favorite_vacancies',
            field=models.ManyToManyField(blank=True, related_name='employees_who_liked', to='job_site.Vacancy'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='favorite_services',
            field=models.ManyToManyField(blank=True, related_name='clients_who_liked', to='job_site.Service'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
    ]
