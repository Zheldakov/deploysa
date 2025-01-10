from gc import get_objects

from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import reverse, render, redirect


from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, user_login_failed
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView

from users.forms import UserLoginForm, UserForm, UserPasswordChangeForm
from users.models import User



def user_login_view(request):
    # Выводим форму логина
    confirmation=True
    if request.method == 'POST':
        form = UserLoginForm(request.POST)  # Создаем экземпляр формы
        print(form.is_valid(),'валидность')
        print(form.errors)
        if form.is_valid(): # Если форма валидна
            cd = form.cleaned_data  #Получаем данные email и password и очищаем форму
            user = authenticate(email=cd['email'], password=cd['password'])  # Аутентифицируем пользователя
            if user is not None:  # Если пользователь существует
                if user.is_active:  # Если пользователь активен
                    login(request, user)  # Авторизуем пользователя
                    return HttpResponseRedirect(reverse('technic:technic_list'))  # Переход на главную страницу с техникой

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

class UserProfileView(DetailView):
    """ Просмотр профиля пользователя."""
    model = User
    form_class = UserForm
    template_name = 'users/profile_user.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        # Добавляем данные в extra_context
        context_data = super().get_context_data(**kwargs)
        object = self.get_object()
        context_data['title'] = f'Профиль пользователя'
        context_data['user_name'] = f'{object.first_name}'
        context_data['user_email'] = f'{object.email}'
        return context_data



class UserUpdateView(UpdateView):
    """ Изменение профиля пользователя."""
    model = User

    form_class = UserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('users:profile_user')

    def get_object(self, queryset=None):
        # Получаем пользователя
        return self.request.user

    def get_context_data(self, **kwargs):
        # Добавляем данные в extra_context
        context_data = super().get_context_data(**kwargs)
        object = self.get_object()
        context_data['title'] = f'Редактирование профиля'
        context_data['user_name'] = f'{object.first_name}'
        context_data['user_email'] = f'{object.email}'
        return context_data

class UserPasswordChangeView(PasswordChangeView):
    """ Изменение пароля пользователя."""
    form_class = UserPasswordChangeForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('technic:technic_list')
    def get_object(self, queryset=None):
        # Получаем пользователя
        return self.request.user

    def get_context_data(self, **kwargs):
        # Добавляем данные в extra_context
        context_data = super().get_context_data(**kwargs)
        object = self.get_object()
        context_data['title'] = f'Редактирование пароля'
        context_data['user_name'] = f'{object.first_name}'
        context_data['user_email'] = f'{object.email}'
        return context_data