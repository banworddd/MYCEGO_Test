import aiohttp
import asyncio



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

def get_files(public_key, token):
    return asyncio.run(fetch_files(public_key, token))
