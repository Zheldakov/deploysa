from django.urls import path

from technic.apps import TechnicConfig
from technic.views import TechnicListView, DepartmentListView, TypeListView, TypeTechnicUpdateView, \
    DepartmentUpdateView, TypeTechnicDeleteView, DepartmentDeleteView, DepartmentCreateView, TypeTechnicCreateView, \
    TechnicDetailView

app_name = TechnicConfig.name

urlpatterns = [
    path('list/', TechnicListView.as_view(), name="technic_list"),  # url список всей техники
    path('detail/<int:pk>', TechnicDetailView.as_view(), name="technic_detail"),  # url список всей техники
    path('type/', TypeListView.as_view(), name="type_list"),  # url список всех типов техники
    path('department/', DepartmentListView.as_view(), name="department_list"),  # url список всех подразделений
    path('type/create/', TypeTechnicCreateView.as_view(), name='type_create'), # создание типов техники
    path('department/create/', DepartmentCreateView.as_view(), name='department_create'), # создание подразделений
    path('type/update/<int:pk>/', TypeTechnicUpdateView.as_view(), name='type_update'), # редактирование типа техники
    path('department/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'), # редактирование подразделений
    path('type/delete/<int:pk>/', TypeTechnicDeleteView.as_view(), name='type_delete'), # удаление типа техники
    path('department/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department_delete'), # удаление подразделений
]
