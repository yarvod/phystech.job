from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from .models import Resume, Vacancy, Employer, Employee, Tag
from .serializers import (
    ResumeListSerializer, ResumeDetailSerializer, ResumeCreateUpdateSerializer,
    VacancyListSerializer, VacancyDetailSerializer, VacancyCreateSerializer,
    EmployerListSerializer, EmployerDetailSerializer,
    EmployeeDetailSerializer,
    UserDetailSerializer,
    TagListSerializer
)


class EmployerListView(ListAPIView):

    queryset = Employer.objects.all()
    serializer_class = EmployerListSerializer


class EmployerDetailView(RetrieveAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerDetailSerializer


class EmployeeDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailSerializer


class VacancyListView(ListAPIView):

    queryset = Vacancy.objects.filter(is_published=True)
    serializer_class = VacancyListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VacancyDetailView(RetrieveAPIView):

    queryset = Vacancy.objects.filter(is_published=True)
    serializer_class = VacancyDetailSerializer


class CreateVacancyView(CreateAPIView):
    serializer_class = VacancyCreateSerializer


class ResumeListView(ListAPIView):

    queryset = Resume.objects.all()
    serializer_class = ResumeListSerializer


class ResumeDetailView(RetrieveAPIView):

    queryset = Resume.objects.all()
    serializer_class = ResumeDetailSerializer


class CreateResumeView(CreateAPIView):
    serializer_class = ResumeCreateUpdateSerializer


class UpdateResumeView(RetrieveUpdateAPIView):
    serializer_class = ResumeCreateUpdateSerializer
    queryset = Resume.objects.all()


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class TagListView(ListAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TagDetailView(RetrieveAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
