# Backend services system for DPM

Это монолит бэкенда, декомпозированный на два логических приложения джанго.
Монолитный сценарий подходит здесь отлично кроме единственного сценария - интеграции.
Для интеграции необходимо использовать 

### Технологии

- python
- пакеты python из `requrements.txt`
- make

### Подготовка и запуск

- установить python в вашей ОС
- установить make в вашей ОС
- склонировать репозиторий
- запустить `make up_service`

### Дополнительно

- при развертке на удаленной машине используйте докер

### Ссылки

- документация django: https://docs.djangoproject.com/en/5.0/
- документация drf: https://www.django-rest-framework.org/topics/documenting-your-api/