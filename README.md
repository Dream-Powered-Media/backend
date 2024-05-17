# Backend services system for DPM

Это монолит бэкенда, декомпозированный на два логических приложения джанго.
Монолитный сценарий подходит здесь отлично кроме единственного сценария - интеграции.
Для интеграции необходимо использовать 

### Технологии

- python
- пакеты python из `requrements.txt`
- make

### Структура

```shell
.
├── content
│   ├── __init__.py
│   └── __pycache__
├── manage.py
├── passport
│   ├── __init__.py
│   ├── __pycache__
│   └── migrations
│       ├── __init__.py
│       └── __pycache__
└── service
    ├── __init__.py
    ├── __pycache__
    └── migrations
        ├── __init__.py
        └── __pycache__
```

### Подготовка и запуск


#### Установка

- установить python в вашей ОС
- установить make в вашей ОС
- склонировать репозиторий


#### Запуск

- запустить `make up_service`
- при необходимости работы в системе нужно зарегистрировать пользователя, либо создать superuser

### Дополнительно

- при развертке на удаленной машине используйте докер

### Ссылки

- документация django: https://docs.djangoproject.com/en/5.0/
- документация drf: https://www.django-rest-framework.org/topics/documenting-your-api/

### API

---

- api/token POST any
- api/v1/token/refresh 
- api/v1/auth/users POST any

- api/v1/auth/users/me GET auth
- api/v1/user/list GET any
- api/v1/user/<pk:uuid>/full-info GET any

---

- api/v1/community/list GET any
- api/v1/community/<pk:uuid>/full-info GET any
- api/v1/community/<pk:uuid>/follow POST auth
- api/v1/community/<pk:uuid>/request-role POST auth
- api/v1/community/<pk:uuid>/change-name PATCH admin
- api/v1/community/<pk:uuid>/change-desc PATCH admin
- api/v1/community/<pk:uuid>/top GET follower
- api/v1/community/<pk:uuid>/add-media PUT participant
- api/v1/community/<pk:uuid>/add-directory PUT admin

---

- api/v1/media/full-list GET any
- api/v1/media/grade POST participant
