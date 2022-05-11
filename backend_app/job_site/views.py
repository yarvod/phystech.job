from users.models import User
from rest_framework import permissions, viewsets
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
    EmployerListSerializer, EmployerDetailSerializer, EmployerCreateUpdateSerializer, 
    EmployeeListSerializer, EmployeeDetailSerializer, EmployeeCreateUpdateSerializer, 
    ClientListSerializer, ClientDetailSerializer, ClientCreateUpdateSerializer,
    FreelancerListSerializer, FreelancerDetailSerializer,FreelancerCreateUpdateSerializer,
    TagListSerializer
)


class EmployerListView(ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerListSerializer


class EmployerDetailView(RetrieveUpdateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerDetailSerializer


class EmployerCreateView(CreateAPIView):
    serializer_class = EmployerCreateUpdateSerializer


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer


class EmployeeDetailView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()\
        .prefetch_related('favorite_vacancies')
    serializer_class = EmployeeDetailSerializer


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeCreateUpdateSerializer


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer


class ClientDetailView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer


class ClientCreateView(CreateAPIView):
    serializer_class = ClientCreateUpdateSerializer


class FreelancerListView(ListAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerListSerializer


class FreelancerDetailView(RetrieveUpdateAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerDetailSerializer


class FreelancerCreateView(CreateAPIView):
    serializer_class = FreelancerCreateUpdateSerializer


class VacancyListView(ListAPIView):

    queryset = Vacancy.objects.filter(is_published=True)
    serializer_class = VacancyListSerializer


class VacancyDetailView(RetrieveAPIView):

    queryset = Vacancy.objects.filter(is_published=True)
    serializer_class = VacancyDetailSerializer


class CreateVacancyView(CreateAPIView):
    serializer_class = VacancyCreateUpdateSerializer


class UpdateVacancyView(RetrieveUpdateAPIView):
    serializer_class = VacancyCreateUpdateSerializer
    queryset = Vacancy.objects.all()


class ResumeListView(ListAPIView):
    queryset = Resume.objects.filter(is_published=True)
    serializer_class = ResumeListSerializer


class ResumeDetailView(RetrieveAPIView):
    queryset = Resume.objects.filter(is_published=True)
    serializer_class = ResumeDetailSerializer


class CreateResumeView(CreateAPIView):
    serializer_class = ResumeCreateUpdateSerializer


class UpdateResumeView(RetrieveUpdateAPIView):
    serializer_class = ResumeCreateUpdateSerializer
    queryset = Resume.objects.all()


class ServiceListView(ListAPIView):
    queryset = Service.objects.filter(is_published=True)
    serializer_class = ServiceListSerializer


class ServiceDetailView(RetrieveAPIView):
    queryset = Service.objects.filter(is_published=True)
    serializer_class = ServiceDetailSerializer


class CreateServiceView(CreateAPIView):
    serializer_class = ServiceCreateUpdateSerializer


class UpdateServiceView(RetrieveUpdateAPIView):
    serializer_class = ServiceCreateUpdateSerializer
    queryset = Service.objects.all()


class TaskListView(ListAPIView):
    queryset = Task.objects.filter(is_published=True)
    serializer_class = TaskListSerializer


class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.filter(is_published=True)
    serializer_class = TaskDetailSerializer


class CreateTaskView(CreateAPIView):
    serializer_class = TaskCreateUpdateSerializer


class UpdateTaskView(RetrieveUpdateAPIView):
    serializer_class = TaskCreateUpdateSerializer
    queryset = Task.objects.all()


class TagListView(ListAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TagDetailView(RetrieveAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
