FROM python:3.8-slim

ENV PYTHONUNBUFFERD=1

RUN apt-get update && apt-get install -y \
    vim less curl

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY pyproject.toml poetry.lock* /app/
WORKDIR /app/
RUN poetry install --no-root

COPY . /app/