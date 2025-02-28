# Описание моделей
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _

# настройка полей, чтобы возможно было заполнить поля пустыми
NULLABLE ={'blank': True, 'null': True}

class UserRoles(models.TextChoices):
    """ Роли пользователь """
    ADMIN = 'admin', _('Администратор')
    MODERATOR = 'moderator', _('Модератор')
    USER = 'user', _('Пользователь')

class User(AbstractUser):
    """Модель пользователя с полями email, телефон и Telegram username."""
    username = None
    email = models.EmailField(unique=True,verbose_name='E-mail')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.USER)
    first_name = models.CharField(max_length=150, verbose_name='Имя',default="Не указано")
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', default="Не указано")
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Телеграм', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватарка', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='active', help_text='Активный пользователь')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return  f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural ='Пользователи'
        ordering = ['id']