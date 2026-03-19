# Use a slim Python image for a smaller attack surface
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install curl for the healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service code
COPY . .

# FIX CKV_DOCKER_2: Create and use a non-root user
RUN useradd -m appuser
USER appuser

# FIX CKV_DOCKER_3: Add a healthcheck to monitor service status
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# Start the application
CMD ["python", "app.py"]