FROM python:3.9-slim

WORKDIR /app

# Install the communication protocol library
RUN pip install paho-mqtt

COPY . .

CMD ["python", "producer.py"]