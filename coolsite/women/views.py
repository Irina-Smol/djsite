from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

#def index(request):
    #return HttpResponse('Главная страница')

def categories(request, catid):
    if (request.GET):  #В консоле отображаются результаты GET запроса в виде "ключ-значение"
        print(request.GET)

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if 2020 < int(year) < 2030:  #Обработка исключения 404 (переход на ошибку 404 ->
        return redirect('home', permanent=True) #отображение функции pageNotFound с результатом "Страница не найдена"
    if int(year) > 2030:
        raise Http404

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)
    #   return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

#передача аргумента в виде словаря (3 атрибут)
# передача из списка menu на главную страницу (отобразить элементы меню в виде списка),
# в index.html передается цикл for где перебираются элементы из menu (список передан выше на 25 строке)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})
#передача аргумента в виде словаря (3 атрибут)

# эти аргументы будут передаваться в шаблоны index.html и about.html в {{ title }}

# сейчас имеются два файла index.html и about.html в которых передана почти одна и та же информация
# нарушается принцип DRY, поэтому создается базовый шаблон base.html

# в базовом шаблоне список menu, который будет отображаться на двух страницах, в других файлах
# наследование базового шаблона

def addpage(request):
    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)