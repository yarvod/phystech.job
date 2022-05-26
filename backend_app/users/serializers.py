from collections import defaultdict

from djoser.serializers import UserSerializer
from rest_framework import serializers

from job_site.serializers import (
    EmployeeUpdateSerializer,
    EmployerUpdateSerializer,
    FreelancerUpdateSerializer,
    ClientUpdateSerializer,
)

from .models import User


class UserDjoserSerializer(UserSerializer):
    employer = EmployerUpdateSerializer(read_only=True)
    employee = EmployeeUpdateSerializer(read_only=True)
    freelancer = FreelancerUpdateSerializer(read_only=True)
    client = ClientUpdateSerializer(read_only=True)
    favorites = serializers.SerializerMethodField()

    @staticmethod
    def get_favorites(obj):
        f = defaultdict(list)
        try:
            ee = obj.employee
            fo = ee.favorite_offers.values_list('id', flat=True)
            fv = ee.favorite_vacancies.values_list('id', flat=True)
            f['vacancies'] = list(fv)
            f['offers'] = list(fo)
        except:
            pass
        try:
            er = obj.employer
            fr = er.favorite_resumes.values_list('id', flat=True)
            f['resumes'] = list(fr)
        except:
            pass
        try:
            ct = obj.client
            fs = ct.favorite_services.values_list('id', flat=True)
            f['services'] = list(fs)
        except:
            pass
        try:
            fer = obj.freelancer
            ft = fer.favorite_tasks.values_list('id', flat=True)
            f['tasks'] = list(ft)
        except:
            pass

        return f

    class Meta:
        model = User
        exclude = ['password']
