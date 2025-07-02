#!/bin/bash
# AutoAgent Django server launcher (background, logs to autoagent_server.log)
cd "$(dirname "$0")"
source ../venv/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 > autoagent_server.log 2>&1 &
echo "AutoAgent server started in background. Log: autoagent_server.log"
