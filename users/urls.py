from django.urls import path

from users.apps import UsersConfig
from users.views import user_login_view, user_logout_view, UserUpdateView, UserPasswordChangeView, UserProfileView, \
    UserListView, AllUserProfileView, ALLUserUpdateView, UserDeleteView, UserCreateView

app_name = UsersConfig.name

urlpatterns = [
    path('', user_login_view, name="login_user"), #  url стартовой страницы для входа
    path('logout/', user_logout_view, name="logout_user"),
    path('profile/', UserProfileView.as_view(), name='profile_user'),
    path('update/', UserUpdateView.as_view(), name="update_user"),
    path('change_password/', UserPasswordChangeView.as_view(), name='change_password_user'),

# просмотр других пользователей
    path('all_users/', UserListView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('profile/<int:pk>/', AllUserProfileView.as_view(), name='profile_all_user'),
    path('update/<int:pk>/', ALLUserUpdateView.as_view(), name='update_all_user'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
]
