from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from .models import (
    Employer, Vacancy,
    Employee, Resume,
    Freelancer, Service,
    Client, Task,
    Tag, Category,
)
from .serializers import (
    ResumeListSerializer, ResumeDetailSerializer, ResumeCreateUpdateSerializer,
    VacancyListSerializer, VacancyDetailSerializer, VacancyCreateUpdateSerializer,
    ServiceListSerializer, ServiceDetailSerializer, ServiceCreateUpdateSerializer,
    TaskListSerializer, TaskDetailSerializer, TaskCreateUpdateSerializer,
    EmployerListSerializer, EmployerDetailSerializer, EmployerUpdateSerializer, EmployerCreateSerializer,
    EmployeeListSerializer, EmployeeDetailSerializer, EmployeeUpdateSerializer, EmployeeCreateSerializer,
    ClientListSerializer, ClientDetailSerializer, ClientUpdateSerializer, ClientCreateSerializer,
    FreelancerListSerializer, FreelancerDetailSerializer, FreelancerUpdateSerializer, FreelancerCreateSerializer,
    TagListSerializer,
    PostInteractActionSerializer,
    CheckEmailSerializer,
)


class EmployerListView(ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerListSerializer


class EmployerDetailView(RetrieveUpdateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerDetailSerializer


class EmployerCreateView(CreateAPIView):
    serializer_class = EmployerCreateSerializer


class EmployerUpdateView(RetrieveUpdateAPIView):
    queryset = Employer.objects.all() \
        .prefetch_related('favorite_resumes')
    serializer_class = EmployerUpdateSerializer


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer


class EmployeeDetailView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()\
        .prefetch_related('favorite_vacancies')
    serializer_class = EmployeeDetailSerializer


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeCreateSerializer


class EmployeeUpdateView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all() \
        .prefetch_related('favorite_vacancies')
    serializer_class = EmployeeUpdateSerializer


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer


class ClientDetailView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer


class ClientCreateView(CreateAPIView):
    serializer_class = ClientCreateSerializer


class ClientUpdateView(RetrieveUpdateAPIView):
    queryset = Client.objects.all() \
        .prefetch_related('favorite_services')
    serializer_class = ClientUpdateSerializer


class FreelancerListView(ListAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerListSerializer


class FreelancerDetailView(RetrieveUpdateAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerDetailSerializer


class FreelancerCreateView(CreateAPIView):
    serializer_class = FreelancerCreateSerializer


class FreelancerUpdateView(RetrieveUpdateAPIView):
    queryset = Freelancer.objects.all() \
        .prefetch_related('favorite_tasks')
    serializer_class = FreelancerUpdateSerializer


class VacancyListView(ListAPIView):

    queryset = Vacancy.objects.filter(is_published=True)
    serializer_class = VacancyListSerializer


class VacancyDetailView(RetrieveAPIView):

    queryset = Vacancy.objects.filter(is_published=True)
    serializer_class = VacancyDetailSerializer


class VacancyCreateView(CreateAPIView):
    serializer_class = VacancyCreateUpdateSerializer


class VacancyUpdateView(RetrieveUpdateAPIView):
    serializer_class = VacancyCreateUpdateSerializer
    queryset = Vacancy.objects.all()


class ResumeListView(ListAPIView):
    queryset = Resume.objects.filter(is_published=True)
    serializer_class = ResumeListSerializer


class ResumeDetailView(RetrieveAPIView):
    queryset = Resume.objects.filter(is_published=True)
    serializer_class = ResumeDetailSerializer


class ResumeCreateView(CreateAPIView):
    serializer_class = ResumeCreateUpdateSerializer


class ResumeUpdateView(RetrieveUpdateAPIView):
    serializer_class = ResumeCreateUpdateSerializer
    queryset = Resume.objects.all()


class ServiceListView(ListAPIView):
    queryset = Service.objects.filter(is_published=True)
    serializer_class = ServiceListSerializer


class ServiceDetailView(RetrieveAPIView):
    queryset = Service.objects.filter(is_published=True)
    serializer_class = ServiceDetailSerializer


class ServiceCreateView(CreateAPIView):
    serializer_class = ServiceCreateUpdateSerializer


class ServiceUpdateView(RetrieveUpdateAPIView):
    serializer_class = ServiceCreateUpdateSerializer
    queryset = Service.objects.all()


class TaskListView(ListAPIView):
    queryset = Task.objects.filter(is_published=True)
    serializer_class = TaskListSerializer


class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.filter(is_published=True)
    serializer_class = TaskDetailSerializer


class TaskCreateView(CreateAPIView):
    serializer_class = TaskCreateUpdateSerializer


class TaskUpdateView(RetrieveUpdateAPIView):
    serializer_class = TaskCreateUpdateSerializer
    queryset = Task.objects.all()


class TagListView(ListAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TagDetailView(RetrieveAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class CheckEmailView(APIView):

    def post(self, request, format=None):
        serializer = CheckEmailSerializer(data=request.data)
        user = User.objects.filter(email=serializer.initial_data.get('email')).first()
        return Response({'exists': bool(user)})
