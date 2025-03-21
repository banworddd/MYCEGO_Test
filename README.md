# MYCEGOTest Application

## Описание

MYCEGOTest — это тестовое задание для компании MYCEGO. Приложение представляет собой веб-интерфейс для просмотра и управления файлами, хранящимися на Яндекс.Диске. Пользователи могут авторизоваться через OAuth, просматривать содержимое папок и скачивать файлы.

## Установка и запуск

### С использованием Docker

1. **Установите Docker**
   - Убедитесь, что Docker и Docker Compose установлены на вашем компьютере.

2. **Сборка Docker-образа**
   - Перейдите в директорию с `docker-compose` и выполните команду для сборки образа:
     ```bash
     docker-compose up --build
     ```
     
   - Эта команда запускает контейнер в фоновом режиме и сопоставляет порт 8000 на вашем хосте с портом 8000 в контейнере.

3**Проверка работы**
   - Откройте браузер и перейдите по адресу `http://localhost:8000`, чтобы увидеть работающее приложение.

### Без использования Docker

1. **Установите Python**
   - Убедитесь, что у вас установлена последняя версия Python

2. **Установите зависимости**
   - Перейдите в директорию с вашим проектом и установите необходимые зависимости:
     ```bash
     pip install -r requirements.txt
     ```

3. **Запуск приложения**
   - Запустите приложение с помощью команды:
     ```bash
     python manage.py runserver
     ```
   - По умолчанию приложение будет доступно по адресу `http://localhost:8000`.

## Использование

1. **Авторизация**
   - Перейдите на страницу авторизации и выполните вход через OAuth Яндекса.

2. **Просмотр файлов**
   - После авторизации вы сможете просматривать содержимое папок и файлов на Яндекс.Диске.

3. **Скачивание файлов**
   - Выберите файлы, которые хотите скачать, и нажмите кнопку "Скачать выбранные файлы".

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле `LICENSE`.

---

**Примечание:** Этот проект является тестовым заданием для компании MYCEGO и демонстрирует навыки работы с Django, Docker и интеграцией с API Яндекс.Диска. Время потраченное на разработку ~ 5  часов

