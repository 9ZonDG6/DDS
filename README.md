# DDS
Веб-сервис для управления движением денежных средств

---
## Требования

* Python ≥3.11
* SQLite
* [uv](https://docs.astral.sh/uv/#project-management) (для управления зависимостями)
---

## Быстрый старт

```bash

uv sync && source venv/bin/activate

cp .env.example .env

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

После запуска сервис будет доступен по адресам:

* **Swagger UI** — [http://localhost:8000/backend/swagger/](http://localhost:8000/backend/swagger/)
* **Redoc** — [http://localhost:8000/backend/redoc/](http://localhost:8000/backend/redoc/)
* **Django‑admin** — [http://localhost:8000/backend/admin/](http://localhost:8000/backend/admin/)
