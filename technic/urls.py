from django.urls import path

from technic.apps import TechnicConfig
from technic.views import TechnicListView, DepartmentListView, TypeListView, TypeTechnicUpdateView, \
    DepartmentUpdateView, TypeTechnicDeleteView, DepartmentDeleteView, DepartmentCreateView, TypeTechnicCreateView

app_name = TechnicConfig.name

urlpatterns = [
    path('list/', TechnicListView.as_view(), name="technic_list"),  # url список всей техники
    path('type/', TypeListView.as_view(), name="type_list"),  # url список всей тех
    path('department/', DepartmentListView.as_view(), name="department_list"),  # url список всей тех
    path('type/create/', TypeTechnicCreateView.as_view(), name='type_create'),
    path('department/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('type/update/<int:pk>/', TypeTechnicUpdateView.as_view(), name='type_update'),
    path('department/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'),
    path('type/delete/<int:pk>/', TypeTechnicDeleteView.as_view(), name='type_delete'),
    path('department/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department_delete'),
]
