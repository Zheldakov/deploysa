from django.urls import path

from technic.apps import TechnicConfig
from technic.views import TechnicListView, DepartmentListView, TypeListView, TypeTechnicUpdateView, \
    DepartmentUpdateView, TypeTechnicDeleteView, DepartmentDeleteView, DepartmentCreateView, TypeTechnicCreateView, \
    TechnicDetailView, TechnicUpdateView, TechnicDeleteView, TechnicCreateView, TechnicListFilterDepartmentView, \
    TechnicListFilterTypeTechnicView, TechnicSearchListView, TechnicServiceUpdateView, ServiceFilterTechnicView, \
    TechnicLostDataView

app_name = TechnicConfig.name

urlpatterns = [
    path('list/', TechnicListView.as_view(), name="technic_list"),  # список всей техники
    path('department/<int:pk>/technic/', TechnicListFilterDepartmentView.as_view(), name='department_technic'), # техника определенного подразделения
    path('type/<int:pk>/technic/', TechnicListFilterTypeTechnicView.as_view(), name='type_technic'), # техника определенного типа
    path('create/', TechnicCreateView.as_view(), name="technic_create"),  # добавление техники
    path('detail/<int:pk>/', TechnicDetailView.as_view(), name="technic_detail"),  # детальная информация по техники
    path('update/<int:pk>/', TechnicUpdateView.as_view(), name="technic_update"),  # редактирование техники
    path('delete/<int:pk>/', TechnicDeleteView.as_view(), name="technic_delete"),  # удаление техники
    path('type/', TypeListView.as_view(), name="type_list"),  # список всех типов техники
    path('department/', DepartmentListView.as_view(), name="department_list"),  # список всех подразделений
    path('type/create/', TypeTechnicCreateView.as_view(), name='type_create'), # создание типов техники
    path('department/create/', DepartmentCreateView.as_view(), name='department_create'), # создание подразделений
    path('type/update/<int:pk>/', TypeTechnicUpdateView.as_view(), name='type_update'), # редактирование типа техники
    path('department/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'), # редактирование подразделений
    path('type/delete/<int:pk>/', TypeTechnicDeleteView.as_view(), name='type_delete'), # удаление типа техники
    path('department/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department_delete'), # удаление подразделений
    path('number/search/', TechnicSearchListView.as_view(), name='technic_search'), # поиск техники по гос номеру
    path('service/<int:pk>/', TechnicServiceUpdateView.as_view(), name='technic_service_update'), # сервис техники
    path('<int:pk>/service/', ServiceFilterTechnicView.as_view(), name='technic_service_list'), # список сервисов по техники
    path('<int:pk>/lost_data/', TechnicLostDataView.as_view(), name='technic_lost_data'), # последние данные от техники
]
