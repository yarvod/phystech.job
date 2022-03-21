from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Resume, Vacancy, Employer
from .serializers import (
    ResumeListSerializer, ResumeDetailSerializer, ResumeCreateSerializer,
    VacancyListSerializer, VacancyDetailSerializer, VacancyCreateSerializer,
    EmployerListSerializer, EmployerDetailSerializer,
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

