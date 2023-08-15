<h1>Инструкция по установки a simple-store-drf</h1>

<h2>Установить к себе репозиторий:</h2>

```
git clone https://github.com/umeliere/store-drf.git
```

---

<h4>Создать файл .env в папке store/core(где находится файл settings.py)<br>
В него занести следующие данные:<br></h4>

```
DEBUG=True
SECRET_KEY=django-insecure-y6_c-qq19+pl_a2_=v*41%^r^1(6525ar+vge8ku&!)-c%)lz!

EMAIL_HOST=XXXXX
EMAIL_PORT=XXXXX
EMAIL_HOST_USER=XXXXX
DEFAULT_FROM_EMAIL=XXXXX
EMAIL_HOST_PASSWORD=XXXXX
EMAIL_USE_SSL=XXXXX

DB_NAME=XXXXX
DB_USER=XXXXX
DB_PASSWORD=XXXXX
DB_HOST=XXXXX
DB_PORT=XXXXX
```
---
<h3>Вам нужно подключить YANDEX smtp, ДОКУМЕНТАЦИЯ:</h3>
http://help.yandex.ru/mail/mail-clients.xml
<p>И заполнить поля:</p>

```
EMAIL_HOST=XXXXX
EMAIL_PORT=XXXXX
EMAIL_HOST_USER=XXXXX
DEFAULT_FROM_EMAIL=XXXXX
EMAIL_HOST_PASSWORD=XXXXX
EMAIL_USE_SSL=XXXXX
```

<p>Если вы не хотите пользоваться yandex smpt, вы всегда можете сменить на любой удобный почтовый сервис</p>

https://docs.djangoproject.com/en/4.2/topics/email/  -- Документация

---

<h3>Также необходимо подключить PostgreSQL и заполнить следующие поля:</h3>

```
DB_NAME=XXXXX
DB_USER=XXXXX
DB_PASSWORD=XXXXX
DB_HOST=XXXXX
DB_PORT=XXXXX
```

<p>Если вы не хотите пользоваться PostgreSQL, вы всегда можете сменить на любую удобную базу данных.</p>

https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes  -- Документация

---

Установить зависимости:

```
pip install -r requirements.txt
```

Произвести миграции:
```
python manage.py makemigrations
python manage.py migrate
```

Создать суперпользователя:
```
python manage.py createsuperuser
```

Запустить сервер(по умолчанию http://localhost:8000):
```
python manage.py runserver
```

---

<h3>API документация доступна по ссылке:</h3>

http://127.0.0.1:8000/swagger/

---
