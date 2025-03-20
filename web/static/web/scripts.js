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

function downloadNextFile(queue) {
    if (queue.length === 0) return;

    const fileUrl = queue.shift();
    downloadFile(fileUrl);

    setTimeout(() => {
        downloadNextFile(queue);
    }, 1000);
}

function downloadFile(url) {
    const link = document.createElement('a');
    link.href = url;
    link.download = '';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}



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