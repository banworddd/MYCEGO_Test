from django.urls import path
from . import views  # Импортируем представления

urlpatterns = [
    path('', views.files_view, name='index'),  # Пример маршрута
]