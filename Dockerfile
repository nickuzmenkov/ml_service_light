FROM python:3.12.2-slim

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ml_service_light ml_service_light
ENTRYPOINT ["streamlit", "run", "--server.fileWatcherType", "none", "ml_service_light/ui.py"]
