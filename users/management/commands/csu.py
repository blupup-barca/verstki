from django.core.management.base import BaseCommand
from users.models import User
class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@email.com")
        user.set.password('1234')
        user.is_staff = True
        user.is_superuser = True
        user.save()