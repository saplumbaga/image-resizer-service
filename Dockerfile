FROM python:2-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT python image_resizer.py