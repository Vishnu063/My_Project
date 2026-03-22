FROM python:3.11-slim
WORKDIR /app
RUN pip install flask flask-cors
COPY app/main.py ./app.py
RUN mkdir -p /data
VOLUME /data
EXPOSE 8000
CMD ["python", "app.py"]
