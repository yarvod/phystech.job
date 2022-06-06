from django.contrib.auth.models import AbstractUser, UserManager
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import JSONField
from django.apps import apps


class CustomUserManager(UserManager):

    def create_user(self, **kwargs):
        username = kwargs.pop('username')
        reg_data = kwargs.get('reg_data')
        if reg_data:
            kwargs.pop('reg_data')
        user = super().create_user(username, **kwargs)
        if reg_data:
            if reg_data.get('as_employee'):
                Employee = apps.get_model('job_site', 'Employee')
                Employee.objects.create(user=user)
            if reg_data.get('as_employer'):
                Employer = apps.get_model('job_site', 'Employer')
                Employer.objects.create(
                    user=user,
                    company_name=reg_data.get('company_name'),
                    company_website=reg_data.get('company_website')
                )
            if reg_data.get('as_client'):
                Client = apps.get_model('job_site', 'Client')
                Client.objects.create(user=user)
            if reg_data.get('as_freelancer'):
                Freelancer = apps.get_model('job_site', 'Freelancer')
                Freelancer.objects.create(user=user)

        return user


class User(AbstractUser):

    show_name = models.BooleanField(default=True)
    show_socials = models.BooleanField(default=True)

    telegram = models.CharField(max_length=50, blank=True, null=True)

    phone_number = models.CharField(max_length=17, blank=True, null=True)

    reg_data = JSONField(encoder=DjangoJSONEncoder, null=True, blank=True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
        'reg_data',
    ]
