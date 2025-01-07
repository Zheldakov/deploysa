from django.urls import path

from technic.apps import TechnicConfig
from technic.views import technic_list_view

app_name = TechnicConfig.name

urlpatterns = [
    path('list/', technic_list_view, name="technic_list"), #  url список всей техники
   ]