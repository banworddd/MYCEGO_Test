import aiohttp
import asyncio
from urllib.parse import quote

async def fetch_files(public_key, token):
    """
    Асинхронно извлекает данные файлов из Яндекс.Диска по публичному ключу.

    Эта функция отправляет HTTP-запрос к API Яндекс.Диска для получения информации о файлах,
    используя предоставленный публичный ключ и токен для аутентификации.

    Аргументы:
        public_key (str): Публичный ключ для доступа к файлам на Яндекс.Диске.
        token (str): Токен OAuth для аутентификации.

    Возвращает:
        dict: Данные файлов в формате JSON, если запрос успешен.

    Выбрасывает:
        Exception: Если запрос не удался, с сообщением об ошибке.
    """
    url = f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}'
    headers = {'Authorization': f'OAuth {token}'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                raise Exception(f"Error fetching data: {response.status} - {await response.text()}")

async def fetch_folder(public_key, token, path):
    """
    Асинхронно извлекает данные папки из Яндекс.Диска по публичному ключу и пути.

    Эта функция отправляет HTTP-запрос к API Яндекс.Диска для получения информации о папке,
    используя предоставленный публичный ключ, токен и путь к папке.

    Аргументы:
        public_key (str): Публичный ключ для доступа к файлам на Яндекс.Диске.
        token (str): Токен OAuth для аутентификации.
        path (str): Путь к папке на Яндекс.Диске.

    Возвращает:
        dict: Данные папки в формате JSON, если запрос успешен.

    Выбрасывает:
        Exception: Если запрос не удался, с сообщением об ошибке.
    """
    encoded_public_key = quote(public_key, safe='')
    encoded_path = quote(path, safe='')

    url = (f'https://cloud-api.yandex.net/v1/disk/public/resources?'
           f'public_key={encoded_public_key}&path={encoded_path}')
    headers = {'Authorization': f'OAuth {token}'}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                raise Exception(f"Error fetching data: {response.status} - {await response.text()}")

def get_folder(public_key, token, path):
    """
    Синхронно извлекает данные папки из Яндекс.Диска.

    Эта функция вызывает асинхронную функцию fetch_folder и возвращает результат.

    Аргументы:
        public_key (str): Публичный ключ для доступа к файлам на Яндекс.Диске.
        token (str): Токен OAuth для аутентификации.
        path (str): Путь к папке на Яндекс.Диске.

    Возвращает:
        dict: Данные папки в формате JSON.
    """
    return asyncio.run(fetch_folder(public_key, token, path))

def get_files(public_key, token):
    """
    Синхронно извлекает данные файлов из Яндекс.Диска.

    Эта функция вызывает асинхронную функцию fetch_files и возвращает результат.

    Аргументы:
        public_key (str): Публичный ключ для доступа к файлам на Яндекс.Диске.
        token (str): Токен OAuth для аутентификации.

    Возвращает:
        dict: Данные файлов в формате JSON.
    """
    return asyncio.run(fetch_files(public_key, token))
