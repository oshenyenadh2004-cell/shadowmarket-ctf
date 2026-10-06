FROM python:3.11-slim

WORKDIR /app
COPY app.py .
COPY ctf.db .

RUN pip install flask

EXPOSE 5000

CMD ["python3", "app.py"]

