from .api_utils import  get_files, get_folder
from .utils import convert_size
from django.shortcuts import render

def files_view(request):
    token = request.session.get('yandex_token')
    folder_link = request.GET.get('folder_link')

    # Если ссылка на папку не передана, не выполняем запрос
    if not folder_link:
        return render(request, 'web/files.html', {
            'files_data': None,
            'error_message': None,
        })

    try:
        data = get_files(folder_link, token)
        parsed_data = parse_and_sort_files(data, token)
        print(parsed_data)
    except Exception as e:
        parsed_data = None
        error_message = str(e)
    else:
        error_message = None

    return render(request, 'web/files.html', {
        'files_data': parsed_data,
        'error_message': error_message,
    })

def parse_and_sort_files(data, token):
    parsed_data = {
        'public_key': data.get('public_key'),
        'public_url': data.get('public_url'),
        'name': data.get('name'),
        'type': data.get('type'),
        'file': data.get('file') if data.get('file') else None,
        'created': data.get('created'),
        'size': convert_size(data.get('size')) if data.get('size') else None,
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
                'size': convert_size(item.get('size', 0)),
                'mime_type': item.get('mime_type'),
                'path': item.get('path'),
                'preview': item.get('preview', '') if item.get('type') == 'file' else '',
                'file': item.get('file') if item.get('type') == 'file' else '',
            }

            if item.get('type') == 'dir':
                folder_data = get_folder(data['public_key'], token, item['path'])
                item_data['items'] = parse_and_sort_files(folder_data, token)['items']

            parsed_data['items'].append(item_data)

        # Сортируем элементы по имени
        parsed_data['items'].sort(key=lambda x: x['name'])

    return parsed_data
