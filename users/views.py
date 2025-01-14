from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import reverse, render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

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
    return render(request, 'users/user_login.html', context)


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
    template_name = 'users/user_create.html'


class UserProfileView(DetailView):
    """ Просмотр профиля пользователя."""
    model = User
    # form_class = UserForm
    template_name = 'users/user_profile.html'
    extra_context = {
        'title': f'Профиль пользователя'
    }

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(UpdateView):
    """ Изменение профиля пользователя."""
    model = User
    form_class = UserForm
    template_name = 'users/user_update.html'
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
    template_name = 'users/password_change.html'
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
    template_name = 'users/users_all.html'
    extra_context = {
        'title': f'Все пользователи'
    }


class AllUserProfileView(DetailView):
    """ Просмотр профиля других пользователей."""
    model = User
    template_name = 'users/user_profile_all.html'
    extra_context = {
        'title': f'Профиль пользователя'
    }


class ALLUserUpdateView(UpdateView):
    """ Изменение профиля других пользователей."""
    model = User
    form_class = UserForm
    template_name = 'users/user_update_all.html'
    extra_context = {
        'title': f'Редактирование профиля'
    }

    def get_success_url(self):
        # Переходим на страницу детальной информацию пользователя после редактирования
        return reverse('users:profile_all_user', args=[self.kwargs.get('pk')])


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    """ Страница удаления пользователя."""
    model = User
    template_name = 'users/user_delete.html'
    # Переходим на страницу со списком питомцев после удаления
    success_url = reverse_lazy('users:users_list')
    permission_required = 'users.delete_user'
