"""
Настройки Django для проекта config.

Сгенерированы с помощью "django-admin startproject" с использованием Django 5.0.9.

Для получения дополнительной информации об этом файле смотрите
https://docs.djangoproject.com/en/5.0/topics/settings/

Полный список настроек и их значений приведен в разделе
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# from django.conf.global_settings import AUTH_USER_MODEL, MEDIA_URL
from dotenv import load_dotenv

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Полный путь к корневому каталогу проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# секретный ключ Django, который должен быть уникальным и безопасным
SECRET_KEY = 'django-insecure-53deg%z)99kaulr1#)6(iw7%f449(i2lbtn_^3b%^qj(a^1q2k'

# SECURITY WARNING: don't run with debug turned on in production!
# Разрешает отключение проверки безопасности во время разработки (DEBUG = False при окончании разработки)
DEBUG = True

# Доменные имена, на которых разрешена публикация проекта
ALLOWED_HOSTS = []

# Application definition
# Набор всех установленных приложений в проекте
INSTALLED_APPS = [
    # базовый функционал
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # добавленные приложения
    'users',
    'technic',
    'news',
]

# плагины и библиотеки
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основной файл с URLS проекта
ROOT_URLCONF = 'config.urls'

# Шаблоны проекта
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# переменная указывает на файл wsgi с переменной application
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# настройки ДБ ( MS SQL Server)
load_dotenv()
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')
HOST = os.getenv('MS_SQL_SERVER')
DATABASE = os.getenv('MS_SQL_DATABASE')
PAD_DATABASE = os.getenv('MS_SQL_PAD_DATABASE')
SU_DJANGO_PASSWORD = os.getenv('SU_DJANGO_PASSWORD')
MODERATOR_PASSWORD = os.getenv('MODERATOR_PASSWORD')
USER_PASSWORD = os.getenv('USER_PASSWORD')
DRIVER = os.getenv('MS_SQL_DRIVER')


DATABASES = {
    'default':{
        'ENGINE': 'mssql',
        'NAME': DATABASE,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': '',
        'OPTIONS':{
            'driver':DRIVER
        }
    }
}

# ниже по умолчанию, настройки Django для подключения к SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
# язык приложений
LANGUAGE_CODE = 'ru-ru'
# временная зона для работы приложения
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Подключение статических файлов (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS =(
        BASE_DIR /'static', # Путь к статическим файлам
)
"""django.views.static.serve()
+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT
прописывается config.urls.py
"""
# Подключение медиа файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = (
    BASE_DIR /'media'
)

"""Поскольку MEDIA_URL определен как '/media/', то config.urls.py добавляется следующая строка
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
# Тип поля первичного ключа по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# добавлена авторизована модель пользователя
AUTH_USER_MODEL = 'users.User'

# задает URL-адрес, на который следует перенаправлять пользователя после успешной авторизации
# LOGIN_REDIRECT_URL = 'tech:all_tech' #'/'

# Определяет URL-адрес, на который перенаправляется пользователь после выхода из системы
# LOGOUT_REDIRECT_URL ='tech:index' #'/'

# Путь, куда попадают не авторизованные пользователи, при использовании функций для авторизованных пользователей
# LOGIN_URL = '/users/'