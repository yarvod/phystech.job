from django.urls import path
from .views import (
    ResumeListView, ResumeDetailView, CreateResumeView,
    VacancyListView, VacancyDetailView, CreateVacancyView,
    EmployerListView, EmployerDetailView,
    EmployeeDetailView,
    UserDetailView,
)


urlpatterns = [
    path("vacancies/", VacancyListView.as_view()),
    path("vacancies/<int:pk>/", VacancyDetailView.as_view()),
    path("vacancy/", CreateVacancyView.as_view()),
    path("resumes/", ResumeListView.as_view()),
    path("resumes/<int:pk>/", ResumeDetailView.as_view()),
    path("resume/", CreateResumeView.as_view()),
    path("employers/", EmployerListView.as_view()),
    path("employers/<int:pk>/", EmployerDetailView.as_view()),
    path("employees/<int:pk>/", EmployeeDetailView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view())
]

