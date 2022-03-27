from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Resume, Vacancy, Employer
from .serializers import (
    ResumeListSerializer, ResumeDetailSerializer, ResumeCreateSerializer,
    VacancyListSerializer, VacancyDetailSerializer, VacancyCreateSerializer,
    EmployerListSerializer, EmployerDetailSerializer,
    UserDetailSerializer
)


class EmployerListView(ListAPIView):

    queryset = Employer.objects.all()
    serializer_class = EmployerListSerializer


class EmployerDetailView(RetrieveAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerDetailSerializer


class VacancyListView(ListAPIView):

    queryset = Vacancy.objects.filter(draft=False, closed=False)
    serializer_class = VacancyListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VacancyDetailView(RetrieveAPIView):

    queryset = Vacancy.objects.filter(draft=False, closed=False)
    serializer_class = VacancyDetailSerializer


class CreateVacancyView(CreateAPIView):
    serializer_class = VacancyCreateSerializer


class ResumeListView(ListAPIView):

    queryset = Resume.objects.filter(draft=False)
    serializer_class = ResumeListSerializer


class ResumeDetailView(RetrieveAPIView):

    queryset = Resume.objects.filter(draft=False)
    serializer_class = ResumeDetailSerializer


class CreateResumeView(CreateAPIView):
    serializer_class = ResumeCreateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

