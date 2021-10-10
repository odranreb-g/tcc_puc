FROM python:3.9.7-slim-buster

RUN pip install poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    python3-dev \
    gcc \
    python3-psycopg2 \
    tzdata \
    gettext \
    && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

ADD . /app/

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "-c", "gunicorn_config.py", "--chdir", "partner_routes_api", "partner_routes_api.wsgi:application", "--graceful-timeout", "30"]
