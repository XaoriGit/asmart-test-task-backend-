FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi --no-root

# Копируем весь проект
COPY . .

# Запуск миграций и сервера
CMD ["sh", "-c", "python manage.py migrate && uvicorn config.asgi:application --host 0.0.0.0 --port 8000"]