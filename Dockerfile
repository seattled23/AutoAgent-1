# Dockerfile for AutoAgent Microservice
#
# Build with: docker build -t autoagent:latest .
# Run with: docker run -d -p 8000:8000 --env-file .env autoagent:latest

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["bash", "run_autoagent_server.sh"]
