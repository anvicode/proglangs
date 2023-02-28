from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# функция представление главной страницы
def index(request):
    """
    request это ссылка на класс HttpRequest
    на выходе формирует экземпляр класса HttpResponse
    """
    return HttpResponse("Страница приложения pl.")


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}<p>")

def archive(request, year):
    if int(year) > 2023:
        return redirect('home')
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}<p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")