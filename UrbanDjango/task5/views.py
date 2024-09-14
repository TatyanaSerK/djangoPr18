from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .UserRegister import UserRegister


def sign_up_by_html(request):
    users = ('Tanya', 'Anya', 'Vanya')
    info = {'error': ['Пароли не совпадают','Вы должны быть старше 18','Пользователь уже существует']}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        error_list = info['error']

        for i in users:
            if i == username:
                error = error_list[2]
                return HttpResponse(f'{error}')

        if int(age) < int(18):
            error = error_list[1]
            return HttpResponse(f'{error}')

        if repeat_password != password:
            error = error_list[0]
            return HttpResponse(f'{error}')

        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = ('Tanya', 'Anya', 'Vanya')
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            repeat_password = form.cleaned_data('repeat_password')
            age = form.cleaned_data('age')

            for i in users:
                if i == username:
                   return HttpResponse("Пользователь уже существует")

            if int(age) < int(18):
                return HttpResponse("Вы должны быть старше 18")

            if repeat_password != password:
                return HttpResponse("Пароли не совпадают")

            return HttpResponse(f'Приветствуем, {username}!')

    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
