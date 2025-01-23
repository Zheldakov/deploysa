from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.shortcuts import reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from pyexpat.errors import messages

from technic.forms import DepartmentForm, TypeTechnicForm, TechnicForm, ServiceForm
from technic.models import Technic, TypeTechnic, Department, Service
from technic.service import get_info


class TechnicListView(ListView):
    """ Список всей техники."""
    model = Technic
    paginate_by = 6
    template_name = 'technic/technic_list.html'
    extra_context = {
        'title': f'Техника'
    }


class TechnicCreateView(CreateView):
    """ Создание техники"""
    model = Technic
    form_class = TechnicForm
    success_url = reverse_lazy('technic:technic_list')
    template_name = 'technic/technic_create.html'
    extra_context = {
        'title': f'Добавление техники'
    }


class TechnicDetailView(DetailView):
    """ Просмотр детальной информации по техники."""
    model = Technic
    template_name = 'technic/technic_detail.html'
    extra_context = {
        'title': f'Детальная информация'
    }


class TechnicUpdateView(UpdateView):
    """ Изменение техники."""
    model = Technic
    form_class = TechnicForm
    template_name = 'technic/technic_update.html'

    def get_success_url(self):
        # Переходим на страницу детальной информации по технике после редактирования
        return reverse('technic:technic_detail', args=[self.kwargs.get('pk')])


class TechnicServiceUpdateView(UpdateView):
    """ Странина сервиса техники"""
    model = Technic
    form_class = TechnicForm
    template_name = 'technic/technic_service_update.html'

    def get_success_url(self):
        # Переходим на страницу детальной информации по технике после редактирования
        return reverse('technic:technic_service_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        # Добавляем форму для редактирования сервисных работ
        contex_data = super().get_context_data(**kwargs)
        ServiceFormset = inlineformset_factory(Technic, Service, form=ServiceForm, extra=1)
        if self.request.method == 'POST':
            formset = ServiceFormset(self.request.POST, instance=self.object)
        else:
            formset = ServiceFormset(instance=self.object)
        contex_data['formset'] = formset
        contex_data['title'] = f'Редактирование техники'
        return contex_data

    def form_valid(self, form):
        # форма валидации для подставления сервиса
        contex_data = self.get_context_data()
        formset = contex_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class TechnicDeleteView(PermissionRequiredMixin, DeleteView):
    """ Страница удаления техники."""
    model = Technic
    template_name = 'technic/technic_delete.html'
    success_url = reverse_lazy('technic:technic_list')
    permission_required = 'technic.delete_technic'
    extra_context = {
        'title': f'Удаление техники'
    }


class DepartmentListView(ListView):
    """ Показывает страницу с информацией о техники определенного подразделения"""
    model = Department
    template_name = 'technic/dep_list.html'
    extra_context = {
        'title': f'Отделения'
    }


class TypeListView(ListView):
    """ Показывает страницу с информацией о техники определенного типа"""
    model = TypeTechnic
    template_name = 'technic/type_list.html'
    extra_context = {
        'title': f'Типы техники'
    }


class DepartmentCreateView(CreateView):
    """ Создание подразделения"""
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('technic:department_list')
    template_name = 'technic/dep_create.html'
    extra_context = {
        'title': f'Создание отделения'
    }


class DepartmentUpdateView(UpdateView):
    """ Изменение подразделения"""
    model = Department
    form_class = DepartmentForm
    template_name = 'technic/dep_update.html'
    success_url = reverse_lazy('technic:department_list')
    extra_context = {
        'title': f'Редактирование отделения'
    }


class DepartmentDeleteView(PermissionRequiredMixin, DeleteView):
    """ Страница удаления подразделения."""
    model = Department
    template_name = 'technic/dep_delete.html'
    success_url = reverse_lazy('technic:department_list')
    permission_required = 'technic.delete_department'
    extra_context = {
        'title': f'Удаление отделения'
    }


class TypeTechnicCreateView(CreateView):
    """ Создание типа техники"""
    model = TypeTechnic
    form_class = TypeTechnicForm
    success_url = reverse_lazy('technic:type_list')
    template_name = 'technic/type_create.html'
    extra_context = {
        'title': f'Создание типа техники'
    }


class TypeTechnicUpdateView(UpdateView):
    """ Изменение типа техники."""
    model = TypeTechnic
    form_class = TypeTechnicForm
    template_name = 'technic/type_update.html'
    success_url = reverse_lazy('technic:type_list')
    extra_context = {
        'title': f'Редактирование отделения'
    }


class TypeTechnicDeleteView(PermissionRequiredMixin, DeleteView):
    """ Страница удаления типа пользователя."""
    model = TypeTechnic
    template_name = 'technic/type_delete.html'
    success_url = reverse_lazy('technic:type_list')
    permission_required = 'technic.delete_typetechnic'
    extra_context = {
        'title': f'Удаление типа техники'
    }


class TechnicListFilterDepartmentView(ListView):
    """ Список всей техники определенного подразделения."""
    model = Technic
    paginate_by = 6
    template_name = 'technic/technic_list.html'
    extra_context = {
        'title': f'Техника'
    }

    def get_queryset(self):
        # Фильтр показывает только технику определенного подразделения
        queryset = super().get_queryset().filter(
            department_id=self.kwargs.get('pk')
        )
        return queryset


class TechnicListFilterTypeTechnicView(ListView):
    """ Список всей техники определенного типа."""
    model = Technic
    paginate_by = 6
    template_name = 'technic/technic_list.html'
    extra_context = {
        'title': f'Техника'
    }

    def get_queryset(self):
        # Фильтр показывает только технику определенного типа
        queryset = super().get_queryset().filter(
            type_id=self.kwargs.get('pk')
        )
        return queryset


class TechnicSearchListView(LoginRequiredMixin, ListView):
    """ Показывает страницу с результатами поиска техники по гос. Номеру."""
    model = Technic
    template_name = 'technic/technic_list.html'
    extra_context = {
        'title': 'Результаты поискового запроса',
    }

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = Technic.objects.filter(Q(number__icontains=query))
        if object_list.exists() == False:
            print("Не найден по гос.номеру")
            object_list = Technic.objects.filter(Q(name__icontains=query))
        if object_list.exists() == False:
            print("Не найден по наименованию")
            object_list = Technic.objects.filter(Q(imei__icontains=query))
        if object_list.exists() == False:
            print("Не найден по IMEI")

        print(object_list)
        return object_list


class ServiceFilterTechnicView(ListView):
    """ Список работ проведенных на технике"""
    model = Service
    paginate_by = 6
    template_name = 'technic/service_list.html'

    def get_queryset(self):
        # Фильтр показывает только сервисы с определенным id техники
        queryset = super().get_queryset().filter(
            technic_id=self.kwargs.get('pk')
        )
        return queryset

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        if self.object_list:
            # если список объектов есть, тогда вписываем первый
            contex_data['name_t'] = self.object_list[0].technic
        contex_data['title'] = f'Список работ на технике'
        return contex_data

class TechnicLostDataView(DetailView):
    model = Technic
    template_name = 'technic/technic_glonass_detail.html'

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        num_technic = self.object.number
        glonass_info = get_info(num_technic)
        contex_data['title'] = f'Последние данные от'
        if glonass_info:
            contex_data['glonass_technic'] = glonass_info['glonass_technic']
            contex_data['glonass_data'] = glonass_info['glonass_data']
            contex_data['glonass_address'] = glonass_info['glonass_address']
            contex_data['glonass_speed'] = glonass_info['glonass_speed']
            contex_data['glonass_geozone'] = glonass_info['glonass_geozone']
        return contex_data
