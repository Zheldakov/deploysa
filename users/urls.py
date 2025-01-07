from django.urls import path

from users.apps import UsersConfig
from users.views import user_login_view,user_logout_view

app_name = UsersConfig.name

urlpatterns = [
    path('', user_login_view, name="login_user"), #  url стартовой страницы для входа
    path('logout/', user_logout_view, name="logout_user"),
]