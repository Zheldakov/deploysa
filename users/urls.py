from django.urls import path

from users.apps import UsersConfig
from users.views import user_login_view,user_logout_view,UserUpdateView,UserPasswordChangeView,UserProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('', user_login_view, name="login_user"), #  url стартовой страницы для входа
    path('logout/', user_logout_view, name="logout_user"),
    path('profile/', UserProfileView.as_view(), name='profile_user'),
    path('update/', UserUpdateView.as_view(), name="update_user"),
    path('change_password/', UserPasswordChangeView.as_view(), name='change_password_user'),
]
