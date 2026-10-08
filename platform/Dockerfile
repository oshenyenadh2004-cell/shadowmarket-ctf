FROM python:3.11-slim
WORKDIR /app
COPY flag_validator.py .
RUN pip install flask
EXPOSE 6001
CMD ["python3", "flag_validator.py"]
