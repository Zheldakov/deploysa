from django.urls import path

from technic.apps import TechnicConfig
from technic.views import TechnicListView, DepartmentListView, TypeListView

app_name = TechnicConfig.name

urlpatterns = [
    path('list/', TechnicListView.as_view(), name="technic_list"), #  url список всей техники
    path('type/', TypeListView.as_view(), name="type_list"), #  url список всей тех
    path('departament/', DepartmentListView.as_view(), name="department_list"), #  url список всей тех
   ]