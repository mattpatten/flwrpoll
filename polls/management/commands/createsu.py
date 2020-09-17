from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="SSAP").exists():
            User.objects.create_superuser(os.environ.get('SUPERUSER_ID'), os.environ.get('SUPERUSER_EMAIL'), os.environ.get('SUPERUSER_PASSWORD'))
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))