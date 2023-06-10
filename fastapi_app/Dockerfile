FROM python:3.11-slim-bullseye
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /src


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat build-essential && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY pyproject.toml poetry.lock ./
RUN pip install -U setuptools && \
    pip install poetry && \
    poetry config virtualenvs.in-project false
RUN poetry install

COPY . ./

CMD poetry run alembic upgrade head && \
    poetry run uvicorn --host=0.0.0.0 app.main:app