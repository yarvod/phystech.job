from rest_framework import serializers
from .models import Vacancy, Resume, Employer


class EmployerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class EmployerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class ResumeListSerializer(serializers.ModelSerializer):
    """Список всех резюме"""
    category = serializers.CharField(source='category.title')
    employee = serializers.CharField(source='employee.user.username')
    likes = serializers.SlugRelatedField(slug_field='company_name', many=True, read_only=True)

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    employee = serializers.CharField(source='employee.user.username')
    likes = serializers.SlugRelatedField(slug_field='company_name', many=True, read_only=True)
    responders = EmployerDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Resume
        exclude = ('draft',)


class ResumeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        exclude = ('draft', 'views', 'likes', 'responders', 'employee')


class VacancyListSerializer(serializers.ModelSerializer):
    """Список всех вакансий"""
    category = serializers.CharField(source='category.title')
    employer = serializers.CharField(source='employer.user.username')
    company_name = serializers.CharField(source='employer.company_name')
    # likes = serializers.SlugRelatedField(slug_field='user.username', many=True, read_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'


class VacancyDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    employer = serializers.CharField(source='employer.user.username')
    company_name = serializers.CharField(source='employer.company_name')
    # likes = serializers.SlugRelatedField(slug_field='', many=True, read_only=True)

    class Meta:
        model = Vacancy
        exclude = ('draft',)


class VacancyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        exclude = ('draft', 'closed', 'views', 'likes', 'responders')

