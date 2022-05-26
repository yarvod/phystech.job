from collections import defaultdict
import logging
import djoser.serializers
from users.models import User
from rest_framework import serializers
from .models import (
    Employer, Vacancy,
    Employee, Resume,
    Freelancer, Service,
    Client, Task,
    Admin, Offer,
    Tag, Category,
    Resume2Vacancy, Vacancy2Resume,
)

debug = logging.getLogger(__name__).debug


class TagListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('title',)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ResumeListSerializer(serializers.ModelSerializer):
    """Список всех резюме"""
    category = serializers.CharField(source='category.title')
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return obj.employers_who_liked.distinct().count()

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeCreateUpdateSerializer(serializers.ModelSerializer):
    employee = serializers.SlugRelatedField(slug_field='id', queryset=Employee.objects.all())
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Resume
        exclude = ('views', )


class VacancyListSerializer(serializers.ModelSerializer):
    """Список всех вакансий"""
    category = serializers.CharField(source='category.title')
    company_name = serializers.CharField(source='employer.company_name')
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return obj.employees_who_liked.distinct().count()

    class Meta:
        model = Vacancy
        fields = '__all__'


class VacancyDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    company_name = serializers.CharField(source='employer.company_name')
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Vacancy
        fields = '__all__'


class VacancyCreateUpdateSerializer(serializers.ModelSerializer):
    employer = serializers.SlugRelatedField(slug_field='id', queryset=Employer.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Vacancy
        exclude = ('views',)


class OfferListSerializer(serializers.ModelSerializer):
    """List of all offers"""
    category = serializers.CharField(source='category.title')
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)
    likes = serializers.SerializerMethodField()

    @staticmethod
    def get_likes(obj):
        return obj.employees_who_liked.distinct().count()

    class Meta:
        model = Offer
        fields = '__all__'


class OfferDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Offer
        fields = '__all__'


class OfferCreateUpdateSerializer(serializers.ModelSerializer):
    admin = serializers.SlugRelatedField(slug_field='id', queryset=Admin.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Offer
        exclude = ('views',)


class ServiceListSerializer(serializers.ModelSerializer):
    """Список всех сервисов"""
    category = serializers.CharField(source='category.title')
    freelancer = serializers.CharField(source='freelancer.user.username')
    likes = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    @staticmethod
    def get_likes(obj):
        return obj.clients_who_liked.distinct().count()

    class Meta:
        model = Service
        fields = '__all__'


class ServiceDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    freelancer = serializers.CharField(source='freelancer.user.username')
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Service
        fields = '__all__'


class ServiceCreateUpdateSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Service
        exclude = ('views',)


class TaskListSerializer(serializers.ModelSerializer):
    """Список всех сервисов"""
    category = serializers.CharField(source='category.title')
    client = serializers.CharField(source='client.user.username')
    likes = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    @staticmethod
    def get_likes(obj):
        return obj.freelancers_who_liked.distinct().count()

    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    client = serializers.CharField(source='client.user.username')
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='title', queryset=Tag.objects.all(), many=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    class Meta:
        model = Task
        exclude = ('views',)


class Resume2VacancyDetailUpdateSerializer(serializers.ModelSerializer):
    from_resume = ResumeDetailSerializer(read_only=True)
    to_vacancy = VacancyDetailSerializer(read_only=True)

    class Meta:
        model = Resume2Vacancy
        fields = '__all__'


class Resume2VacancyListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume2Vacancy
        fields = '__all__'


class EmployerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'


class EmployerDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', required=False)
    company_name = serializers.CharField(required=False)
    vacancies = VacancyDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Employer
        fields = '__all__'


class EmployerCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employer
        fields = '__all__'


class EmployerUpdateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', required=False)
    company_name = serializers.CharField(required=False)
    favorite_resumes_id = serializers.SlugRelatedField(source='favorite_resumes',
                                                       slug_field='id', queryset=Resume.objects.all(), many=True)
    favorite_resumes = ResumeDetailSerializer(many=True, required=False)
    vacancies = VacancyDetailSerializer(read_only=True, many=True)
    r2v = serializers.SerializerMethodField()

    def get_r2v(self, instance):
        data = Resume2Vacancy.objects.filter(to_vacancy__employer=instance)
        return Resume2VacancyDetailUpdateSerializer(data, many=True).data

    def update(self, instance, validated_data):
        company_name = validated_data.get('company_name')
        if company_name:
            instance.company_name = company_name

        f_r = validated_data.get('favorite_resumes')
        if f_r:
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

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', required=False)
    favorite_vacancies_id = serializers.SlugRelatedField(source='favorite_vacancies', required=False,
                                                         slug_field='id', queryset=Vacancy.objects.all(), many=True)
    favorite_vacancies = VacancyDetailSerializer(read_only=True, many=True, required=False)
    favorite_offers_id = serializers.SlugRelatedField(source='favorite_offers', required=False,
                                                         slug_field='id', queryset=Offer.objects.all(), many=True)
    favorite_offers = OfferDetailSerializer(read_only=True, many=True, required=False)
    resumes = ResumeDetailSerializer(read_only=True, many=True)
    r2v = serializers.SerializerMethodField()

    def get_r2v(self, instance):
        data = Resume2Vacancy.objects.filter(from_resume__employee=instance)
        return Resume2VacancyDetailUpdateSerializer(data, many=True).data

    def update(self, instance, validated_data):
        f_v = validated_data.get('favorite_vacancies')
        f_o = validated_data.get('favorite_offers')
        if f_v:
            try:
                f_v = f_v[0]
                f_v_id = f_v.id
            except:
                return instance

            try:
                v = instance.favorite_vacancies.get(id=f_v_id)
                instance.favorite_vacancies.remove(v)
            except:
                instance.favorite_vacancies.add(f_v_id)

        if f_o:
            try:
                f_o = f_o[0]
                f_o_id = f_o.id
            except:
                return instance

            try:
                o = instance.favorite_offers.get(id=f_o_id)
                instance.favorite_offers.remove(o)
            except:
                instance.favorite_offers.add(f_o_id)

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
    user = serializers.CharField(source='user.username', required=False)
    services = ServiceDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Freelancer
        fields = '__all__'


class FreelancerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Freelancer
        fields = '__all__'


class FreelancerUpdateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', required=False)
    favorite_tasks = TaskDetailSerializer(read_only=True, many=True)
    favorite_tasks_id = serializers.SlugRelatedField(source='favorite_tasks',
                                                     slug_field='id', queryset=Task.objects.all(), many=True)
    services = ServiceDetailSerializer(read_only=True, many=True)

    def update(self, instance, validated_data):
        f_t = validated_data.pop('favorite_tasks')
        debug('f_t', f_t)
        try:
            f_t = f_t[0]
            f_t_id = f_t.id
            debug('f_t_id ', f_t_id)
        except:
            return instance

        try:
            t = instance.favorite_tasks.get(id=f_t_id)
            debug('t ', t)
            instance.favorite_tasks.remove(t)
        except:
            instance.favorite_tasks.add(f_t_id)

        instance.save()
        return instance

    class Meta:
        model = Freelancer
        fields = '__all__'


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', required=False)
    tasks = TaskDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Client
        fields = '__all__'


class ClientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ClientUpdateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', required=False)
    favorite_services = ServiceDetailSerializer(read_only=True, many=True)
    favorite_services_id = serializers.SlugRelatedField(source='favorite_services',
                                                        slug_field='id', queryset=Service.objects.all(), many=True)
    tasks = TaskDetailSerializer(read_only=True, many=True)

    def update(self, instance, validated_data):
        f_s = validated_data.pop('favorite_services')
        debug('f_s', f_s)
        try:
            f_s = f_s[0]
            f_s_id = f_s.id
            debug('f_s_id ', f_s_id)
        except:
            return instance

        try:
            s = instance.favorite_services.get(id=f_s_id)
            debug('s ', s)
            instance.favorite_services.remove(s)
        except:
            instance.favorite_services.add(f_s_id)

        instance.save()
        return instance

    class Meta:
        model = Client
        fields = '__all__'


class PostInteractActionSerializer(serializers.Serializer):
    ACTION_CHOICES = (
        'like',
        'response'
    )

    action = serializers.ChoiceField(ACTION_CHOICES)


class CheckEmailSerializer(serializers.Serializer):
    email = serializers.CharField()

