# AdventureWorks API

A Django REST Framework (DRF) API built on top of the AdventureWorks PostgreSQL database. Includes Redis caching, JWT authentication, and is deployed on Heroku.

---

## 🚀 Features

- Django 5 + DRF
- PostgreSQL (AdventureWorks schema)
- Redis integration via django-redis
- JWT Authentication
- Paginated API
- Docker + Heroku deployment ready
- Environment-specific `.env` support

---

## 🛠 Tech Stack

- Django 5.2
- djangorestframework
- django-environ
- psycopg2-binary
- django-redis
- djangorestframework-simplejwt
- Heroku (Postgres + Redis)

---

## 📦 Installation (Local)

```bash
git clone https://github.com/your-username/adventureworks-api.git
cd adventureworks-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # and update with local values
python manage.py runserver
```
## for local setup of adventureworks db checkout issue 1 or readme of original repo
https://github.com/lorint/AdventureWorks-for-Postgres
