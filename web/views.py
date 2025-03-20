from django.shortcuts import render
from .api_utils import  get_files, get_folder
def files_view(request):
    token = 'y0__xDFurDEBxj1nDYgxNPxyxIxtNPaRMrGN0O0PQ4ual9EjZTCkg'
    folder_link = 'https://disk.yandex.ru/d/BQgyGxy-jLQRqA'
    data = get_files(folder_link, token)
    parsed_data = parse_and_sort_files(data, token)
    print(parsed_data)
    return render(request, 'web/files.html',  {'files_data': parsed_data})


def parse_and_sort_files(data, token):
    parsed_data = {
        'public_key': data.get('public_key'),
        'public_url': data.get('public_url'),
        'name': data.get('name'),
        'created': data.get('created'),
        'modified': data.get('modified'),
        'owner': data.get('owner', {}).get('display_name'),
        'items': []
    }

    if '_embedded' in data and 'items' in data['_embedded']:
        for item in data['_embedded']['items']:
            item_data = {
                'name': item.get('name'),
                'type': item.get('type'),
                'created': item.get('created'),
                'modified': item.get('modified'),
                'size': item.get('size', 0),
                'mime_type': item.get('mime_type'),
                'path': item.get('path'),
                'preview': item.get('preview', '') if item.get('type') == 'file' else ''
            }

            # Если это папка, рекурсивно получаем её содержимое
            if item.get('type') == 'dir':
                folder_data = get_folder(data['public_key'], token, item['path'])
                item_data['items'] = parse_and_sort_files(folder_data, token)['items']

            parsed_data['items'].append(item_data)

        # Сортируем элементы по имени
        parsed_data['items'].sort(key=lambda x: x['name'])

    return parsed_data
