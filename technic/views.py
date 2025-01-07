from django.shortcuts import reverse, render, redirect

def technic_list_view(request):
    """ Показывает страницу со списком всей техники."""
    user = request.user

    context = {
        'title': "Вся техника",
        'user_name': user.first_name,
        'user_email': user.email,
    }

    return render(request, 'technic/technic_list.html', context)  # тестовый вариант