from django.core.management import call_command
from django.core.management.base import BaseCommand

from links.models import Link


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        Link.objects.all().delete()

        call_command("loaddata", "link_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
