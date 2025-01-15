from django.urls import path

from technic.apps import TechnicConfig
from technic.views import TechnicListView, DepartmentListView, TypeListView, TypeTechnicUpdateView, \
    DepartmentUpdateView, TypeTechnicDeleteView, DepartmentDeleteView, DepartmentCreateView, TypeTechnicCreateView, \
    TechnicDetailView, TechnicUpdateView, TechnicDeleteView

app_name = TechnicConfig.name

urlpatterns = [
    path('list/', TechnicListView.as_view(), name="technic_list"),  # список всей техники
    path('detail/<int:pk>', TechnicDetailView.as_view(), name="technic_detail"),  # детальная информация по техники
    path('update/<int:pk>', TechnicUpdateView.as_view(), name="technic_update"),  # редактирование техники
    path('delete/<int:pk>', TechnicDeleteView.as_view(), name="technic_delete"),  # удаление техники
    path('type/', TypeListView.as_view(), name="type_list"),  # список всех типов техники
    path('department/', DepartmentListView.as_view(), name="department_list"),  # список всех подразделений
    path('type/create/', TypeTechnicCreateView.as_view(), name='type_create'), # создание типов техники
    path('department/create/', DepartmentCreateView.as_view(), name='department_create'), # создание подразделений
    path('type/update/<int:pk>/', TypeTechnicUpdateView.as_view(), name='type_update'), # редактирование типа техники
    path('department/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'), # редактирование подразделений
    path('type/delete/<int:pk>/', TypeTechnicDeleteView.as_view(), name='type_delete'), # удаление типа техники
    path('department/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department_delete'), # удаление подразделений
]
