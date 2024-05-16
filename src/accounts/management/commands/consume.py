from django.core.management.base import BaseCommand

from src.accounts.consumer import UserCreatedConsumer


class Command(BaseCommand):
    help = 'Launches Listener for user_created message : RaabitMQ'  # noqa

    def handle(self, *args, **options):
        td = UserCreatedConsumer()
        td.start()
        self.stdout.write('Started Consumer Thread')
