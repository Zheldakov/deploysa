from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import reverse, render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, user_login_failed
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, ListView, DeleteView, CreateView

from users.forms import UserLoginForm, UserForm, UserPasswordChangeForm, UserCreateForm
from users.models import User


def user_login_view(request):
    # Выводим форму логина
    confirmation = True
    if request.method == 'POST':
        form = UserLoginForm(request.POST)  # Создаем экземпляр формы
        print(form.is_valid(), 'валидность')
        print(form.errors)
        if form.is_valid():  # Если форма валидна
            cd = form.cleaned_data  # Получаем данные email и password и очищаем форму
            user = authenticate(email=cd['email'], password=cd['password'])  # Аутентифицируем пользователя
            if user is not None:  # Если пользователь существует
                if user.is_active:  # Если пользователь активен
                    login(request, user)  # Авторизуем пользователя
                    return HttpResponseRedirect(
                        reverse('technic:technic_list'))  # Переход на главную страницу с техникой

                else:
                    return HttpResponse('Аккаунт не активен')
            else:
                confirmation = False

    form = UserLoginForm()
    context = {
        'form': form,
        'user': confirmation}
    return render(request, 'users/login_user.html', context)


def user_logout_view(request):
    # выход из системы
    print("выход из системы")
    logout(request)
    return redirect('users:login_user')

class UserCreateView(CreateView):
    """ Создание пользователя."""
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('users:users_list')
    template_name = 'users/create_user.html'

class UserProfileView(DetailView):
    """ Просмотр профиля пользователя."""
    model = User
    # form_class = UserForm
    template_name = 'users/profile_user.html'
    extra_context = {
        'title': f'Профиль пользователя'
    }

    def get_object(self, queryset=None):
        return self.request.user

    # def get_context_data(self, **kwargs):
    #     # Добавляем данные в extra_context
    #     context_data = super().get_context_data(**kwargs)
    #     object = self.get_object()
    #     context_data['title'] = f'Профиль пользователя'
    #     context_data['user_name'] = f'{object.first_name}'
    #     context_data['user_email'] = f'{object.email}'
    #     return context_data


class UserUpdateView(UpdateView):
    """ Изменение профиля пользователя."""
    model = User
    form_class = UserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('users:profile_user')
    extra_context = {
        'title': f'Редактирование профиля'
    }

    def get_object(self, queryset=None):
        # Получаем пользователя
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    """ Изменение пароля пользователя."""
    form_class = UserPasswordChangeForm
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('technic:technic_list')
    extra_context = {
        'title': f'Редактирование пароля'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = User.objects.get(pk=self.request.user.id)
        context["object.pk"] = obj.id
        return context


# Для работы с остальными пользователями (для админа)
class UserListView(LoginRequiredMixin, ListView):
    """ Список всех пользователей."""
    model = User
    paginate_by = 6
    template_name = 'users/all_users.html'
    extra_context = {
        'title': f'Все пользователи'
    }

    # def get_queryset(self):
    #     # фильтр показывает только активных пользователей
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_active=True)
    #     return queryset


class AllUserProfileView(DetailView):
    """ Просмотр профиля других пользователей."""
    model = User
    template_name = 'users/profile_all_user.html'
    extra_context = {
        'title': f'Профиль пользователя'
    }


class ALLUserUpdateView(UpdateView):
    """ Изменение профиля других пользователей."""
    model = User
    form_class = UserForm
    template_name = 'users/update_all_user.html'
    extra_context = {
        'title': f'Редактирование профиля'
    }


    def get_success_url(self):
        # Переходим на страницу детальной информацию пользователя после редактирования
        return reverse('users:profile_all_user', args=[self.kwargs.get('pk')])

class UserDeleteView(PermissionRequiredMixin, DeleteView):
    """ Страница удаления пользователя."""
    model = User
    template_name = 'users/delete_user.html'
    # Переходим на страницу со списком питомцев после удаления
    success_url = reverse_lazy('users:users_list')
    permission_required = 'users.delete_user'