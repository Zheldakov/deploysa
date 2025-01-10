"""
Настройка URL-адресов для проекта config.

Список `urlpatterns` перенаправляет URL-адреса в представления. Для получения дополнительной информации, пожалуйста, смотрите:
 https://docs.djangoproject.com/en/5.0/topics/http/urls/
Примеры:
Функциональные представления
 1. Добавьте импорт: из my_app импортируйте представления
 2. Добавьте URL-адрес в urlpatterns: path(", views.home, name="home")
Представления на основе классов
 1. Добавьте импорт: из other_app.views импортируйте Home
 2. Добавьте URL-адрес в urlpatterns: path(", Home.as_view(), name="home")
Включая другой URLconf
 1. Импортируйте функцию include(): из django.urls импортируйте include, path
 2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
"""Отслеживание url-адресов"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# urls для административной панели Django
urlpatterns = [
                  path('admin_panel/', admin.site.urls),  # URL для административной панели Django
                  path('', include('users.urls', namespace='users')),  # URL для приложения users
                path('technic/', include('technic.urls', namespace='technic')), # URL для приложения technic
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Добавляем медиафайлы