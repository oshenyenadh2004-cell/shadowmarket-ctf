FROM python:3.11-slim
WORKDIR /app
COPY platform/portal/app.py .
COPY platform/portal/templates templates
COPY stage1-osint static/stage1-osint
COPY stage2-stego static/stage2-stego
COPY stage3-crypto static/stage3-crypto
COPY stage5-forensics static/stage5-forensics
COPY stage6-network static/stage6-network
RUN pip install flask requests
EXPOSE 8080
CMD ["python3", "app.py"]
