

from django.shortcuts import reverse, render, redirect
from django.views.generic import ListView

from technic.models import Technic, TypeTechnic, Department


# def technic_list_view(request):
#     """ Показывает страницу со списком всей техники."""
#     user = request.user
#     context = {
#         'title': "Вся техника",
#         'user_name': user.first_name,
#         'user_email': user.email,
#     }
#     return render(request, 'technic/technic_list.html', context)  # тестовый вариант

class TechnicListView(ListView):
    """ Список всей техники."""
    model = Technic
    paginate_by = 6
    template_name = 'technic/technic_list.html'
    extra_context = {
        'title': f'Техника'
    }


# class TypeListView(ListView):
#     """ Показывает страницу с информацией о техники определенного типа."""
#     model = TypeTechnic
#     template_name = 'technic/type_list.html'
#
#     def get_queryset(self):
#         # Фильтр показывает только активную определенного типа технику
#         queryset = super().get_queryset().filter(
#             typetechnic_id=self.kwargs.get('pk'), is_active=True
#         )
#         return queryset
#
class DepartmentListView(ListView):
    """ Показывает страницу с информацией о техники определенного подразделения"""
    model = Department
    template_name = 'technic/dep_type_list.html'


class TypeListView(ListView):
    """ Показывает страницу с информацией о техники определенного типа"""
    model = TypeTechnic
    template_name = 'technic/dep_type_list.html'
