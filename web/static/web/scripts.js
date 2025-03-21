// Функция для скачивания выбранных файлов
function downloadSelectedFiles() {
    const checkboxes = document.querySelectorAll('.file-checkbox:checked');

    if (checkboxes.length === 0) {
        alert('Выберите хотя бы один файл для скачивания.');
        return;
    }

    const downloadQueue = [];
    checkboxes.forEach(checkbox => {
        const fileUrl = checkbox.getAttribute('data-url');
        if (fileUrl) {
            downloadQueue.push(fileUrl);
        }
    });

    downloadNextFile(downloadQueue);
}

// Функция для скачивания следующего файла из очереди
function downloadNextFile(queue) {
    if (queue.length === 0) return;

    const fileUrl = queue.shift();
    downloadFile(fileUrl);

    setTimeout(() => {
        downloadNextFile(queue);
    }, 1000);
}

// Функция для скачивания файла по URL
function downloadFile(url) {
    const link = document.createElement('a');
    link.href = url;
    link.download = '';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Обработчик события загрузки DOM
document.addEventListener('DOMContentLoaded', function () {
    const folders = document.querySelectorAll('.folder-container');

    folders.forEach(folder => {
        const header = folder.querySelector('.folder-header');
        const content = folder.nextElementSibling; // Содержимое папки находится снизу

        if (content && content.classList.contains('folder-content')) {
            header.addEventListener('click', function () {
                content.classList.toggle('open');
            });
        }
    });
});

// Обработчик события загрузки DOM для фильтрации файлов
document.addEventListener('DOMContentLoaded', function () {
    const filterSelect = document.getElementById('mime-type-filter');
    const fileList = document.getElementById('file-list');

    // Функция для рекурсивной фильтрации элементов
    function filterItems(items, selectedType) {
        items.forEach(item => {
            const isFolder = item.querySelector('.folder-container') !== null; // Проверяем, является ли элемент папкой
            const nestedItems = item.querySelectorAll('.folder-content .file-item'); // Вложенные элементы

            if (isFolder) {
                // Если это папка, проверяем её вложенные элементы
                let hasVisibleItems = false;

                nestedItems.forEach(nestedItem => {
                    const mimeType = nestedItem.getAttribute('data-mime-type'); // Получаем mime_type вложенного элемента

                    // Показываем или скрываем вложенный элемент в зависимости от выбранного типа
                    if (selectedType === 'all' || mimeType.startsWith(selectedType)) {
                        nestedItem.style.display = 'block'; // Показываем элемент
                        hasVisibleItems = true; // Папка содержит хотя бы один видимый элемент
                    } else {
                        nestedItem.style.display = 'none'; // Скрываем элемент
                    }
                });

                // Показываем папку, если она содержит хотя бы один видимый элемент
                if (hasVisibleItems) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            } else {
                // Если это файл, применяем фильтрацию
                const mimeType = item.getAttribute('data-mime-type'); // Получаем mime_type файла

                // Показываем или скрываем элемент в зависимости от выбранного типа
                if (selectedType === 'all' || mimeType.startsWith(selectedType)) {
                    item.style.display = 'block'; // Показываем элемент
                } else {
                    item.style.display = 'none'; // Скрываем элемент
                }
            }
        });
    }

    filterSelect.addEventListener('change', function () {
        const selectedType = this.value; // Выбранный тип файла
        const fileItems = fileList.querySelectorAll('.file-item'); // Все элементы списка

        // Применяем фильтрацию ко всем элементам
        filterItems(fileItems, selectedType);
    });
});
