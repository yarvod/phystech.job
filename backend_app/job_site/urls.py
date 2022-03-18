from django.urls import path
from rest_framework import routers
from .views import \
    ResumeListView, ResumeDetailView, \
    VacancyListView, VacancyDetailView


urlpatterns = [
    path("vacancies/", VacancyListView.as_view()),
    path("vacancies/<int:pk>/", VacancyDetailView.as_view()),
    path("resumes/", ResumeListView.as_view()),
    path("resumes/<int:pk>/", ResumeDetailView.as_view())
]


# router = routers.DefaultRouter()
#
# router.register(r'resumes', ResumeListView)
# router.register(r'resumes/<int:pk>/', ResumeDetailView)
# router.register(r'vacancies', VacancyListView)
# router.register(r'vacancies/<int:pk>/', VacancyDetailView)
#
# urlpatterns = router.urls
