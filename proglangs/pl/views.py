from django.http import HttpResponse
# from django.shortcuts import render


# функция представление главной страницы
def index(request):
    """
    request это ссылка на класс HttpRequest
    на выходе формирует экземпляр класса HttpResponse
    """
    return HttpResponse("Страница приложения pl.")


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")
