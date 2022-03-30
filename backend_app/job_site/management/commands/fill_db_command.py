from django.core.management import BaseCommand
from job_site.fill_db import fill_db


class Command(BaseCommand):

    def handle(self, *args, **options):

        fill_db()
        
