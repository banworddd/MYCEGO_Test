from django.shortcuts import render, redirect
import requests

def index_view(request):
    """
    Отображает главную страницу приложения.

    Эта функция представления рендерит шаблон 'users/index.html' для отображения главной страницы.

    Аргументы:
        request: Объект HTTP-запроса.

    Возвращает:
        Отображаемая HTML-страница.
    """
    return render(request, 'users/index.html')

def auth_view(request):
    """
    Отображает страницу авторизации.

    Эта функция представления рендерит шаблон 'users/auth.html' для отображения страницы авторизации.

    Аргументы:
        request: Объект HTTP-запроса.

    Возвращает:
        Отображаемая HTML-страница.
    """
    return render(request, 'users/auth.html')

def oauth_callback(request):
    """
    Обрабатывает обратный вызов OAuth для получения токена доступа.

    Эта функция извлекает код авторизации из запроса, обменивает его на токен доступа
    и сохраняет токен в сессии пользователя.

    Аргументы:
        request: Объект HTTP-запроса, содержащий код авторизации.

    Возвращает:
        Перенаправляет на страницу с файлами или отображает страницу с ошибкой.
    """
    code = request.GET.get('code')
    if not code:
        return render(request, 'users/error.html', {'error': 'Ошибка авторизации'})

    client_id = 'ae0c928ddcaf459fafad23a4a40082bc'
    client_secret = '1b03ef55d7e54ac3b9b0c897f0e00d79'
    redirect_uri = 'http://localhost:8000/oauth_callback/'

    token_url = 'https://oauth.yandex.ru/token'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        request.session['yandex_token'] = access_token

        return redirect('files_view')
    else:
        return render(request, 'users/error.html', {'error': 'Ошибка получения токена'})

def yandex_auth(request):
    """
    Инициирует процесс авторизации через OAuth Яндекса.

    Эта функция перенаправляет пользователя на страницу авторизации Яндекса для получения кода авторизации.

    Аргументы:
        request: Объект HTTP-запроса.

    Возвращает:
        Перенаправляет на страницу авторизации Яндекса.
    """
    client_id = 'ae0c928ddcaf459fafad23a4a40082bc'
    redirect_uri = 'http://localhost:8000/oauth_callback/'
    auth_url = (
        f'https://oauth.yandex.ru/authorize?response_type=code&'
        f'client_id={client_id}&redirect_uri={redirect_uri}'
    )
    return redirect(auth_url)

def logout_view(request):
    """
    Выполняет выход пользователя из системы.

    Эта функция удаляет токен Яндекса из сессии пользователя и перенаправляет его на страницу с файлами.

    Аргументы:
        request: Объект HTTP-запроса.

    Возвращает:
        Перенаправляет на страницу с файлами.
    """
    if 'yandex_token' in request.session:
        del request.session['yandex_token']
    return redirect('files_view')
