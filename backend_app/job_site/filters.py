from django_filters import rest_framework as filters
from job_site.models import (
    Resume2Vacancy,
)


class Resume2VacancyFilter(filters.FilterSet):
    employee = filters.BaseInFilter(field_name='from_resume__employee')
    employer = filters.BaseInFilter(field_name='to_vacancy__employer')

    class Meta:
        model = Resume2Vacancy
        fields = ('from_resume', 'to_vacancy')
