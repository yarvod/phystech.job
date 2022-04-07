from .models import *
from django.contrib.auth.models import User


def fill_db():

    u1 = User.objects.filter(username='ivan').first()
    if not u1:
        u1 = User.objects.create_user(
            username='ivan',
            first_name='Иван',
            last_name='Иванов',
            email='ivan@mail.ru',
            password='ivanpassword'
        )
        u1.save()

    u2 = User.objects.filter(username='alex').first()
    if not u2:
        u2 = User.objects.create_user(
            username='alex',
            first_name='Алексей',
            last_name='Алексеев',
            email='alex@mail.ru',
            password='alexpassword'
        )
        u2.save()

    u3 = User.objects.filter(username='mike').first()
    if not u3:
        u3 = User.objects.create_user(
            username='mike',
            first_name='Михаил',
            last_name='Михайлов',
            email='mike@mail.ru',
            password='mikepassword'
        )
        u3.save()

    u4 = User.objects.filter(username='sasha').first()
    if not u4:
        u4 = User.objects.create_user(
            username='sasha',
            first_name='Александр',
            last_name='Александров',
            email='sasha@mail.ru',
            password='sashapassword'
        )
        u4.save()

    ee1 = Employee.objects.filter(user__username=u1.username).first()
    if not ee1:
        ee1 = Employee(user=u1)
        ee1.save()

    ee2 = Employee.objects.filter(user__username=u2.username).first()
    if not ee2:
        ee2 = Employee(user=u2)
        ee2.save()

    er1 = Employer.objects.update_or_create(user=u3)[0]
    er1.company_name = 'Компания Михаила'
    er1.save()
    er2 = Employer.objects.update_or_create(user=u4)[0]
    er2.company_name = 'Компания Александра'
    er2.save()

    c1 = Category.objects.update_or_create(title='IT', slug='it')[0]
    c2 = Category.objects.update_or_create(title='Science', slug='sc')[0]
    c3 = Category.objects.update_or_create(title='Business', slug='bz')[0]
    c4 = Category.objects.update_or_create(title='Management', slug='mn')[0]

    Tag.objects.update_or_create(code='python', title='Python')
    Tag.objects.update_or_create(code='c', title='C')
    Tag.objects.update_or_create(code='c++', title='C++')
    Tag.objects.update_or_create(code='js', title='JavaScript')
    Tag.objects.update_or_create(code='django', title='Django')


    fields = dict(
        employee=ee1,
        about_me=f'Резюме {ee1.user.first_name}а. ' * 10,
        category=c1,
        is_published=True
    )
    Resume.objects.update_or_create(title=f'Резюме {ee1.user.first_name}а. ', defaults=fields)

    fields = dict(
        employee=ee2,
        about_me=f'Резюме {ee2.user.first_name}а. ' * 10,
        category=c2,
        is_published=True
    )
    Resume.objects.update_or_create(title=f'Резюме {ee2.user.first_name}а. ', defaults=fields)



    fields = dict(
        employer=er1,
        about=f'Вакансия {er1.user.first_name}а .' * 10,
        category=c3,
        is_published=True
    )
    Vacancy.objects.update_or_create(title=f'Вакансия {er1.user.first_name}а .', defaults=fields)

    fields = dict(
        employer=er2,
        about=f'Вакансия {er1.user.first_name}а .' * 10,
        category=c4,
        is_published=True
    )
    Vacancy.objects.update_or_create(title=f'Вакансия {er2.user.first_name}а .', defaults=fields)


if __name__ == '__main__':
    fill_db()
