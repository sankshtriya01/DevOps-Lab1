FROM python:3.13-slim

WORKDIR /app

COPY app/ ./app/

CMD ["python3", "app/app.py"]
