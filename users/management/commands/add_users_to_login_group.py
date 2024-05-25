from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class Command(BaseCommand):
    help = 'Add users to Login Users group'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='login_users')
        if created:
            self.stdout.write(self.style.SUCCESS('Created group login_users'))
        else:
            self.stdout.write(self.style.WARNING('Group login_users already exists'))

        # Укажите нужных пользователей
        emails = ['dmitrylepyansky@yandex.ru']  # Замените на нужные email-адреса
        users = User.objects.filter(email__in=emails)

        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found to add to login_users group'))
            return

        for user in users:
            if not user.groups.filter(name='login_users').exists():
                user.groups.add(group)
                self.stdout.write(self.style.SUCCESS(f'Added {user.email} to login_users group'))
            else:
                self.stdout.write(self.style.WARNING(f'User {user.email} is already in login_users group'))
