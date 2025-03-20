def convert_size(size_bytes):

    units = ['байт', 'КБ', 'МБ', 'ГБ', 'ТБ']

    unit_index = 0
    size = size_bytes

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    size = round(size, 2)

    return f"{size} {units[unit_index]}"