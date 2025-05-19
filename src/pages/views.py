from tempfile import template

from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    title = 'Главная страница фильмов'
    promo = 'Матрица'
    context = {
        'title': title,
        'promo': promo,
    }
    return render(request, template_name, context)


def about(request):
    template_name = 'about/about.html'
    title = 'Страница О'
    promo = 'Тут информация о приложении'
    context = {
        'title': title,
        'promo': promo,
    }
    return render(request, template_name, context)


def movies_list(request):
    template_name = 'categories/movies_list.html'
    context = [
        {
            'id': 1,
            'title': 'Название фильма',
        },
        {
            'id': 2,
            'title': 'Второй фильм',
        },
    ]
    return render(request, template_name, {'movies': context})


def series_list(request):
    template_name = 'categories/series_list.html'
    return render(request, template_name)


def login(request):
    template_name = 'register/login.html'
    return render(request, template_name)


def register(request):
    template_name = 'register/register.html'

    return render(request, template_name)


def movie_item(request, pk):
    template_name = 'categories/movie_detail.html'
    print(f'Это ID фильма {pk}')
    context = {
        'id': pk,
        'title': 'Название фильма',
    }
    return render(request, template_name, {'movies': context})
