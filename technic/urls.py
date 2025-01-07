from django.urls import path

from users.apps import UsersConfig
from technic.views import technic_list_view

app_name = UsersConfig.name

urlpatterns = [
    path('list/', technic_list_view, name="technic_list"), #  url список всей техники
   ]