FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
RUN adduser --disabled-password --gecos "" thor && chown -R thor:thor /app
USER thor
EXPOSE 5000
CMD ["python", "app.py" ]
