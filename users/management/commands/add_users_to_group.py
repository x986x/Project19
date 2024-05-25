from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class Command(BaseCommand):
    help = 'Add users to Moderators group'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Moderators')
        if created:
            self.stdout.write(self.style.SUCCESS('Created group Moderators'))
        else:
            self.stdout.write(self.style.WARNING('Group Moderators already exists'))

        # Укажите нужных пользователей
        emails = ['dmitry.lepyansky@yandex.ru']
        users = User.objects.filter(email__in=emails)

        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found to add to Moderators group'))
            return

        for user in users:
            if not user.groups.filter(name='Moderators').exists():
                user.groups.add(group)
                self.stdout.write(self.style.SUCCESS(f'Added {user.email} to Moderators group'))
            else:
                self.stdout.write(self.style.WARNING(f'User {user.email} is already in Moderators group'))