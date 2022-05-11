from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.apps import apps


class User(AbstractUser):

    telegram = models.CharField(max_length=50, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    as_employee = models.BooleanField(default=False)
    as_employer = models.BooleanField(default=False)
    as_client = models.BooleanField(default=False)
    as_freelancer = models.BooleanField(default=False)

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'as_employee',
        'as_employer',
        'as_client',
        'as_freelancer',
    ]

    def save(self, *args, **kwargs):
        if self.is_active:
            if self.as_employee:
                try:
                    self.employee
                except:
                    Employee = apps.get_model('job_site', 'Employee')
                    e, c = Employee.objects.get_or_create(user=self)
            if self.as_employer:
                try:
                    self.employer
                except:
                    Employer = apps.get_model('job_site', 'Employer')
                    e, c = Employer.objects.get_or_create(user=self)
            if self.as_freelancer:
                try:
                    self.freelancer
                except:
                    Freelancer = apps.get_model('job_site', 'Freelnacer')
                    e, c = Freelancer.objects.get_or_create(user=self)
            if self.as_client:
                try:
                    self.client
                except:
                    Client = apps.get_model('job_site', 'Client')
                    e, c = Client.objects.get_or_create(user=self)

        super().save(*args, **kwargs)
