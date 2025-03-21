from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse

def convert_size(size_bytes: int) -> str:
    """
    Конвертирует размер в байтах в более крупные единицы измерения (КБ, МБ, ГБ, ТБ).

    Эта функция принимает размер в байтах и возвращает его в наиболее подходящем формате
    с округлением до двух знаков после запятой.

    Аргументы:
        size_bytes (int): Размер в байтах, который нужно конвертировать.

    Возвращает:
        str: Размер в удобочитаемом формате с указанием единицы измерения (байт, КБ, МБ, ГБ, ТБ).
    """
    units = ['байт', 'КБ', 'МБ', 'ГБ', 'ТБ']

    unit_index = 0
    size = size_bytes

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    size = round(size, 2)

    return f"{size} {units[unit_index]}"

def yandex_token_required(redirect_url: str = 'index'):
    """
    Декоратор для проверки наличия yandex_token в сессии.
    Если токен отсутствует, перенаправляет на указанную страницу.
    """
    def decorator(view_func):
        def wrapper(request: HttpRequest, *args, **kwargs) -> HttpResponse:
            if not request.session.get('yandex_token'):
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
