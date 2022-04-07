import djoser.serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Vacancy, Resume, Employer, Employee


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
        exclude = ('published',)


class ResumeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        exclude = ('published', 'views', 'employee')


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
        exclude = ('published',)


class VacancyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        exclude = ('views',)


class EmployerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class EmployerDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Employer
        fields = '__all__'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    resumes = ResumeDetailSerializer(read_only=True, many=True)
    favorite_vacancies = VacancyDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class UserDetailSerializer(djoser.serializers.UserSerializer):
    employer = EmployerDetailSerializer(read_only=True)
    employee = EmployeeDetailSerializer(read_only=True, source='Employee')

    class Meta:
        model = User
        exclude = ['password']
