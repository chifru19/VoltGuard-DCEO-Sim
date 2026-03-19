FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
COPY . .
RUN useradd -m appuser
USER appuser
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/health || exit 1
CMD ["python", "utility_logic.py"]