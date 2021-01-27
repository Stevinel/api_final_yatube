# Описание

Проект представляет собой API для проекта yatube.

Функционал:
Авторизацию по JWT токену
Сериализацию данных для всех моделей проекта (Post, Comment, Group, Follow)
Обработку GET, POST, PATCH, PUT и DELETE запросов к базе данных проекта Yatube

# Установка

Склонировать репозиторий
Создать и активировать виртуальное окружение для проекта

python -m venv venv

source venv/scripts/activate

Установить зависимости
python pip install -r requirements.txt

Сделать миграции
python manage.py makemigrations
python manage.py migrate

Запустить сервер
python manage.py runserver

#Примеры
