from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Resume, Vacancy
from .serializers import \
    ResumeListSerializer, ResumeDetailSerializer, \
    VacancyListSerializer, VacancyDetailSerializer


class VacancyListView(APIView):

    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancyListSerializer(vacancies, many=True)
        return Response(serializer.data)


class VacancyDetailView(APIView):

    def get(self, request, pk):
        vacancies = Vacancy.objects.get(id=pk)
        serializer = VacancyDetailSerializer(vacancies)
        return Response(serializer.data)


class ResumeListView(APIView):

    def get(self, request):
        resumes = Resume.objects.all()
        serializer = ResumeListSerializer(resumes, many=True)
        return Response(serializer.data)


class ResumeDetailView(APIView):

    def get(self, request, pk):
        resume = Resume.objects.get(id=pk)
        serializer = ResumeDetailSerializer(resume)
        return Response(serializer.data)
