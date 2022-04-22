from collections import defaultdict
import logging
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

debug = logging.getLogger(__name__).debug


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
        exclude = ('views', )


class VacancyListSerializer(serializers.ModelSerializer):
    """Список всех вакансий"""
    category = serializers.CharField(source='category.title')
    employer_id = serializers.CharField(source='employer.id')
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
    employer_id = serializers.CharField(source='employer.id')
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
    favorite_resumes_id = serializers.SlugRelatedField(source='favorite_resumes',
                                                       slug_field='id', queryset=Resume.objects.all(), many=True)
    favorite_resumes = ResumeDetailSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        f_r = validated_data.pop('favorite_vacancies')
        debug('f_r', f_r)
        try:
            f_r = f_r[0]
            f_r_id = f_r.id
            debug('f_r_id ', f_r_id)
        except:
            return instance

        try:
            r = instance.favorite_resumes.get(id=f_r_id)
            debug('r ', r)
            instance.favorite_resumes.remove(r)
        except:
            instance.favorite_resumes.add(f_r_id)

        instance.save()
        return instance


class Meta:
        model = Employer
        fields = '__all__'


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', required=False)
    resumes = ResumeDetailSerializer(read_only=True, many=True)
    favorite_vacancies_id = serializers.SlugRelatedField(source='favorite_vacancies',
                                                         slug_field='id', queryset=Vacancy.objects.all(), many=True)
    favorite_vacancies = VacancyDetailSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        f_v = validated_data.pop('favorite_vacancies')
        debug('f_v', f_v)
        try:
            f_v = f_v[0]
            f_v_id = f_v.id
            debug('f_v_id ', f_v_id)
        except:
            return instance

        try:
            v = instance.favorite_vacancies.get(id=f_v_id)
            debug('v ', v)
            instance.favorite_vacancies.remove(v)
        except:
            instance.favorite_vacancies.add(f_v_id)

        instance.save()
        return instance

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
    favorites = serializers.SerializerMethodField()

    @staticmethod
    def get_favorites(obj):
        f = defaultdict(list)
        try:
            ee = obj.employee
            fv = ee.favorite_vacancies.values_list('id', flat=True)
            f['vacancies'] = list(fv)
        except:
            pass
        try:
            er = obj.employer
            fr = er.favorite_resumes.values_list('id', flat=True)
            f['resumes'] = list(fr)
        except:
            pass
        try:
            ct = obj.client
            fs = ct.favorite_services.values_list('id', flat=True)
            f['services'] = list(fs)
        except:
            pass
        try:
            fer = obj.freelancer
            ft = fer.favorite_tasks.values_list('id', flat=True)
            f['tasks'] = list(ft)
        except:
            pass

        return f


    class Meta:
        model = User
        exclude = ['password']


class TagListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
