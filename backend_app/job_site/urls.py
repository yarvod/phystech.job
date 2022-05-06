from django.urls import path
from .views import (
    ResumeListView, ResumeDetailView, CreateResumeView, UpdateResumeView,
    VacancyListView, VacancyDetailView, CreateVacancyView, UpdateVacancyView,
    TaskListView, TaskDetailView, CreateTaskView, UpdateTaskView,
    ServiceListView, ServiceDetailView, CreateServiceView, UpdateServiceView,
    EmployerListView, EmployerDetailView, EmployerCreateView,
    EmployeeListView, EmployeeDetailView, EmployeeCreateView,
    UserDetailView,
    TagListView, TagDetailView,
)


urlpatterns = [
    path("vacancies/", VacancyListView.as_view()),
    path("vacancies/<int:pk>/", VacancyDetailView.as_view()),
    path("vacancy/", CreateVacancyView.as_view()),
    path("vacancy/<int:pk>/", UpdateVacancyView.as_view()),
    path("resumes/", ResumeListView.as_view()),
    path("resumes/<int:pk>/", ResumeDetailView.as_view()),
    path("resume/", CreateResumeView.as_view()),
    path("resume/<int:pk>/", UpdateResumeView.as_view()),
    path("services/", ServiceListView.as_view()),
    path("services/<int:pk>/", ServiceDetailView.as_view()),
    path("service/", CreateServiceView.as_view()),
    path("service/<int:pk>/", UpdateServiceView.as_view()),
    path("tasks/", TaskListView.as_view()),
    path("tasks/<int:pk>/", TaskDetailView.as_view()),
    path("task/", CreateTaskView.as_view()),
    path("task/<int:pk>/", UpdateTaskView.as_view()),
    path("employer/", EmployerCreateView.as_view()),
    path("employers/", EmployerListView.as_view()),
    path("employers/<int:pk>/", EmployerDetailView.as_view()),
    path("employee/", EmployeeCreateView.as_view()),
    path("employees/", EmployeeListView.as_view()),
    path("employees/<int:pk>/", EmployeeDetailView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("tags/", TagListView.as_view()),
    path("tags/<int:pk>/", TagDetailView.as_view()),
]

