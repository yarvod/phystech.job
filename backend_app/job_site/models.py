from django.contrib.auth.models import User

from django.urls import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    title = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Resume(models.Model):

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='resumes')

    title = models.CharField(max_length=255)
    about_me = models.TextField(null=True, blank=True)
    work_experiance = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)

    location = models.CharField(max_length=100, null=True, blank=True)
    ready_relocate = models.BooleanField(default=False)
    ready_distant_work = models.BooleanField(default=False)

    file = models.FileField(null=True, blank=True)

    views = models.IntegerField(default=0)

    category = TreeForeignKey(Category, on_delete=models.PROTECT, related_name='resumes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='resumes')

    is_published = models.BooleanField(default=False)
    published = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Vacancy(models.Model):

    employer = models.ForeignKey('Employer', on_delete=models.CASCADE, related_name='vacancies')

    title = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True)
    duties = models.TextField(null=True, blank=True)  # обязанности
    requirements = models.TextField(null=True, blank=True)  # требования
    skills = models.TextField(null=True, blank=True)   #  навыки
    conditions = models.TextField(null=True, blank=True)  # условия

    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)

    location = models.CharField(max_length=255, null=True, blank=True)

    distant_work = models.BooleanField(default=False)

    category = TreeForeignKey(Category, on_delete=models.PROTECT, related_name='vacancies')
    tags = models.ManyToManyField(Tag, blank=True, related_name='vacancies')

    views = models.IntegerField(default=0)

    is_published = models.BooleanField(default=False)
    published = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vacancies'


class Employee(models.Model):
    user = models.OneToOneField(User, related_name='Employee', on_delete=models.CASCADE)

    favorite_vacancies = models.ManyToManyField('Vacancy', blank=True, related_name='employees_who_like')

    def __str__(self):
        return self.user.username


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)

    favorite_resumes = models.ManyToManyField('Resume', blank=True, related_name='employers_who_liked')

    def __str__(self):
        return self.company_name


class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
