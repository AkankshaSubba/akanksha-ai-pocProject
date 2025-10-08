FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENV FLASK_APP=app.py
CMD ["gunicorn", "--bind", "127.0.0.1", "app:app"]