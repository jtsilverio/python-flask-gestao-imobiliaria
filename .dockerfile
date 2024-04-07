ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code

RUN apt-get update && apt-get install make

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
   pip install --upgrade pip && \
   pip install -r /tmp/requirements.txt --no-deps && \
   rm -rf /root/.cache/

COPY . /code

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "main:main"]