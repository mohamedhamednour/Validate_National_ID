FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --cache-dir=/root/.pip -r /code/requirements.txt

COPY ./start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

COPY . /code/

ENTRYPOINT ["/start.sh"]
