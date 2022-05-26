from django.urls import path
from .views import (
    ResumeListView, ResumeDetailView, ResumeCreateView, ResumeUpdateView,
    VacancyListView, VacancyDetailView, VacancyCreateView, VacancyUpdateView,
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView,
    ServiceListView, ServiceDetailView, ServiceCreateView, ServiceUpdateView,
    OfferListView, OfferDetailView, OfferUpdateView, OfferCreateView,
    EmployerListView, EmployerDetailView, EmployerCreateView, EmployerUpdateView,
    EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView,
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView,
    FreelancerListView, FreelancerDetailView, FreelancerCreateView, FreelancerUpdateView,
    TagListView, TagDetailView,
    CategoryListView,
    CheckEmailView,
    Resume2VacancyListCreateView, Resume2VacancyDetailUpdateView,
)


urlpatterns = [
    path("vacancies/", VacancyListView.as_view()),
    path("vacancies/<int:pk>/", VacancyDetailView.as_view()),
    path("vacancy/", VacancyCreateView.as_view()),
    path("vacancy/<int:pk>/", VacancyUpdateView.as_view()),
    path("offers/", OfferListView.as_view()),
    path("offers/<int:pk>/", OfferDetailView.as_view()),
    path("offer/", OfferCreateView.as_view()),
    path("offer/<int:pk>/", OfferUpdateView.as_view()),
    path("resumes/", ResumeListView.as_view()),
    path("resumes/<int:pk>/", ResumeDetailView.as_view()),
    path("resume/", ResumeCreateView.as_view()),
    path("resume/<int:pk>/", ResumeUpdateView.as_view()),
    path("services/", ServiceListView.as_view()),
    path("services/<int:pk>/", ServiceDetailView.as_view()),
    path("service/", ServiceCreateView.as_view()),
    path("service/<int:pk>/", ServiceUpdateView.as_view()),
    path("tasks/", TaskListView.as_view()),
    path("tasks/<int:pk>/", TaskDetailView.as_view()),
    path("task/", TaskCreateView.as_view()),
    path("task/<int:pk>/", TaskUpdateView.as_view()),
    path("employer/", EmployerCreateView.as_view()),
    path("employer/<int:pk>/", EmployerUpdateView.as_view()),
    path("employers/", EmployerListView.as_view()),
    path("employers/<int:pk>/", EmployerDetailView.as_view()),
    path("employee/", EmployeeCreateView.as_view()),
    path("employee/<int:pk>/", EmployeeUpdateView.as_view()),
    path("employees/", EmployeeListView.as_view()),
    path("employees/<int:pk>/", EmployeeDetailView.as_view()),
    path("client/", ClientCreateView.as_view()),
    path("client/<int:pk>/", ClientUpdateView.as_view()),
    path("clients/", ClientListView.as_view()),
    path("clients/<int:pk>/", ClientDetailView.as_view()),
    path("freelancer/", FreelancerCreateView.as_view()),
    path("freelancer/<int:pk>/", FreelancerUpdateView.as_view()),
    path("freelancers/", FreelancerListView.as_view()),
    path("freelancers/<int:pk>/", FreelancerDetailView.as_view()),
    path("tags/", TagListView.as_view()),
    path("tags/<int:pk>/", TagDetailView.as_view()),
    path("categories/", CategoryListView.as_view()),
    path("check_email/", CheckEmailView.as_view()),
    path("resumes2vacancies/", Resume2VacancyListCreateView.as_view()),
    path("resumes2vacancies/<int:pk>/", Resume2VacancyDetailUpdateView.as_view())
]

