FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN mkdir -p /app/output
RUN pip install kafka-python lxml
CMD ["python", "main.py"]
