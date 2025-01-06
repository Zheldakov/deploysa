"""Команда создания администратора Django (DjangoAdmin)"""
from django.core.management import BaseCommand

from users.models import User
from config.settings import SU_DJANGO_PASSWORD,MODERATOR_PASSWORD,USER_PASSWORD


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin = User.objects.create(
            email='admin@ca.ru',
            first_name='Admin',
            last_name='Adminov',
            role = 'admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        admin.set_password(SU_DJANGO_PASSWORD)
        admin.save()
        print('Админcратор создан')
    
        moderator = User.objects.create(
            email='moderator@ca.ru',
            first_name='Moderator',
            last_name='Moderator',
            role='moderator',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )
        moderator.set_password(MODERATOR_PASSWORD)
        moderator.save()
        print('Модератор создан')

        user = User.objects.create(
            email='user@ca.ru',
            first_name='User',
            last_name='User',
            role='user',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )
        user.set_password(USER_PASSWORD)
        user.save()
        print('Пользователь создан')
