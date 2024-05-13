ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code
COPY database/db.sqlite3 /code/database/db.sqlite3

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
   pip install --upgrade pip && \
   pip install -r /tmp/requirements.txt --no-deps && \
   rm -rf /root/.cache/

COPY . /code

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "main:create_app()"]