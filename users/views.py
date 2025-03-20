from django.shortcuts import render, redirect
import requests

def auth_view(request):

    return render(request, 'users/auth.html')


def oauth_callback(request):

    code = request.GET.get('code')  # Код авторизации
    if not code:
        return render(request, 'users/error.html', {'error': 'Ошибка авторизации'})

    # Получаем токен
    client_id = 'ae0c928ddcaf459fafad23a4a40082bc'  # Замените на ваш client_id
    client_secret = '1b03ef55d7e54ac3b9b0c897f0e00d79'
    redirect_uri = 'http://localhost:8000/oauth_callback/'  # Замените на ваш redirect_uri

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
        access_token = token_data.get('access_token')  # Временный токен
        print(access_token)
        # Сохраняем токен в сессии
        request.session['yandex_token'] = access_token

        return redirect('files_view')  # Перенаправляем на страницу с файлами
    else:
        return render(request, 'users/error.html', {'error': 'Ошибка получения токена'})

def yandex_auth(request):

    client_id = 'ae0c928ddcaf459fafad23a4a40082bc'  # Замените на ваш client_id
    redirect_uri = 'http://localhost:8000/oauth_callback/'  # Замените на ваш redirect_uri
    auth_url = (
        f'https://oauth.yandex.ru/authorize?response_type=code&'
        f'client_id={client_id}&redirect_uri={redirect_uri}'
    )
    return redirect(auth_url)