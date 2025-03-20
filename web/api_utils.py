import aiohttp
import asyncio
from urllib.parse import quote


async def fetch_files(public_key, token):
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
    return asyncio.run(fetch_folder(public_key, token, path))

def get_files(public_key, token):
    return asyncio.run(fetch_files(public_key, token))
