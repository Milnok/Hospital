# Hospital
Установка:

Скачиваем: `git clone github.com/Milnok/Hospital`

Заходим в консоль, переходим в папку с проектом

Создаем виртуальное окружение: `python -m venv venv`

Активируем виртуальное окружение: `venv\scripts\activate`

Устанавливаем пакеты: `pip install -r requirements.txt`

Создаем миграции: `python manage.py makemigrations`

Создаем базу данных: `python manage.py migrate`

Создаем суперпользователя: `python manage.py createsuperuser`

Запускаем сервер `python manage.py runserver`

Для работы нужно создать в админке докторов и пациентов, заходим в браузере `http://127.0.0.1:8000/admin`

Можно работать с API через `http://127.0.0.1:8000` или оконное приложение `github.com/Milnok/Hospital_window_PyQt5`
