from .models import *
from django.contrib.auth.models import User


def fill_db():
    user1 = User.objects.update_or_create(username='user1', defaults=dict(password='user1_pass_phystech'))[0]

    user2 = User.objects.update_or_create(username='user2', defaults=dict(password='user2_pass_phystech'))[0]

    employee = Employee.objects.update_or_create(user=user1)[0]

    employer = Employer.objects.update_or_create(user=user2)[0]
    employer.company_name = 'Company 1'

    category = Category.objects.update_or_create(title='IT', slug='it')[0]

    Tag.objects.update_or_create(code='python', title='Python')
    Tag.objects.update_or_create(code='c', title='C')
    Tag.objects.update_or_create(code='c++', title='C++')
    Tag.objects.update_or_create(code='js', title='JavaScript')
    Tag.objects.update_or_create(code='django', title='Django')


    for i in range(6):
        fields = dict(
            employee=employee,
            body=f'Resume {i}'+f'Resume {i}'+f'Resume {i}',
            category=category
        )
        Resume.objects.update_or_create(title=f'Resume {i}', defaults=fields)

    for i in range(6):
        fields = dict(
            employer=employer,
            body=f'Vacancy {i}'+f'Vacancy {i}'+f'Vacancy {i}',
            category=category
        )
        Vacancy.objects.update_or_create(title=f'Vacancy {i}', defaults=fields)
