FROM python:2-slim

COPY . /app
WORKDIR /app

ENV AUTH_TOKEN=default_auth_token

RUN pip install -r requirements.txt

ENTRYPOINT python image_resizer.py