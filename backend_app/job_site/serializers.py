import djoser.serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    Employer, Vacancy,
    Employee, Resume,
    Freelancer, Service,
    Client, Task,
    Tag, Category,
)


class ResumeListSerializer(serializers.ModelSerializer):
    """Список всех резюме"""
    category = serializers.CharField(source='category.title')
    employee = serializers.CharField(source='employee.user.username')

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    employee = serializers.CharField(source='employee.user.username')
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return obj.employers_who_liked.distinct().count()

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeCreateUpdateSerializer(serializers.ModelSerializer):
    employee = serializers.SlugRelatedField(slug_field='id', queryset=Employee.objects.all())
    tags = serializers.SlugRelatedField(slug_field='code', queryset=Tag.objects.all(), many=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Resume
        exclude = ('views')


class VacancyListSerializer(serializers.ModelSerializer):
    """Список всех вакансий"""
    category = serializers.CharField(source='category.title')
    employer = serializers.CharField(source='employer.user.username')
    company_name = serializers.CharField(source='employer.company_name')
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return obj.employees_who_liked.distinct().count()

    class Meta:
        model = Vacancy
        fields = '__all__'


class VacancyDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    employer = serializers.CharField(source='employer.user.username')
    company_name = serializers.CharField(source='employer.company_name')

    class Meta:
        model = Vacancy
        fields = '__all__'


class VacancyCreateUpdateSerializer(serializers.ModelSerializer):
    employer = serializers.SlugRelatedField(slug_field='id', queryset=Employer.objects.all())
    tags = serializers.SlugRelatedField(slug_field='code', queryset=Tag.objects.all(), many=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Vacancy
        exclude = ('views',)


class ServiceListSerializer(serializers.ModelSerializer):
    """Список всех сервисов"""
    category = serializers.CharField(source='category.title')
    freelancer = serializers.CharField(source='freelancer.user.username')
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return obj.clients_who_liked.distinct().count()

    class Meta:
        model = Service
        fields = '__all__'


class ServiceDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    freelancer = serializers.CharField(source='freelancer.user.username')

    class Meta:
        model = Vacancy
        exclude = ('published',)


class ServiceCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        exclude = ('views',)


class TaskListSerializer(serializers.ModelSerializer):
    """Список всех сервисов"""
    category = serializers.CharField(source='category.title')
    client = serializers.CharField(source='client.user.username')
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return obj.freelancers_who_liked.distinct().count()

    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    client = serializers.CharField(source='client.user.username')

    class Meta:
        model = Task
        exclude = ('published',)


class TaskCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ('views',)


class EmployerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class EmployerDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    vacancies = VacancyDetailSerializer(read_only=True, many=True)
    favorite_resumes = ResumeDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Employer
        fields = '__all__'


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    resumes = ResumeDetailSerializer(read_only=True, many=True)
    favorite_vacancies = VacancyDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class FreelancerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = '__all__'


class FreelancerDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    services = ServiceDetailSerializer(read_only=True, many=True)
    favorite_tasks = TaskDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    tasks = TaskDetailSerializer(read_only=True, many=True)
    favorite_services = ServiceDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Client
        fields = '__all__'


class UserDetailSerializer(djoser.serializers.UserSerializer):
    employer = EmployerDetailSerializer(read_only=True)
    employee = EmployeeDetailSerializer(read_only=True)
    freelancer = FreelancerDetailSerializer(read_only=True)
    client = ClientDetailSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ['password']


class TagListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
