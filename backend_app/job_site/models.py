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

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title


class Resume(models.Model):

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    body = models.TextField()
    file = models.FileField(null=True, blank=True)

    draft = models.BooleanField(default=False)

    likes = models.ManyToManyField('Employer', blank=True, related_name='liked_resumes')

    category = TreeForeignKey(Category, on_delete=models.PROTECT, related_name='resumes')

    created = models.DateTimeField(auto_now_add=True)


class Vacancy(models.Model):

    employer = models.ForeignKey('Employer', on_delete=models.CASCADE, related_name='vacancies')

    title = models.CharField(max_length=255)
    body = models.TextField()

    draft = models.BooleanField(default=False)

    category = TreeForeignKey(Category, on_delete=models.PROTECT, related_name='vacancies')

    likes = models.ManyToManyField('Employee', blank=True, related_name='liked_vacancies')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vacancies'


class Employee(models.Model):
    user = models.OneToOneField(User, related_name='Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
