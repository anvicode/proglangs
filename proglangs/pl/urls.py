from django.urls import path

from .views import *

# все маршруты текущего приложения
urlpatterns = [
    path('', index),  # http://127.0.0.1:8000/pl/
    path('cats/', categories),  # http://127.0.0.1:8000/pl/cats/
]
