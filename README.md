# Описание

Проект представляет собой API для проекта yatube.

Функционал:
Авторизация по JWT токену

Сериализация данных для всех моделей проекта (Post, Comment, Group, Follow)

Обработка GET, POST, PATCH, PUT и DELETE запросов к базе данных проекта Yatube

# Установка

## 1)Склонировать репозиторий
## 2)Создать и активировать виртуальное окружение для проекта

python -m venv venv

source venv/scripts/activate

## 3)Установить зависимости
python pip install -r requirements.txt

## 4)Сделать миграции
python manage.py makemigrations
python manage.py migrate

## 5)Запустить сервер
python manage.py runserver

# Примеры

Для доступа к API необходимо получить токен: 
Для этого создать POST-запрос localhost:8000/api/v1/token/ передав поля username и password. API вернет токен.

Дальше, передав токен можно будет обращаться к методам, например: 

/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)

