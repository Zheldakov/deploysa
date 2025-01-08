from django.shortcuts import reverse, render, redirect


from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm


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