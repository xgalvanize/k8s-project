FROM python:3.11-slim
ENV DEBIAN_FRONTEND=noninteractive
# Install system dependencies for WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    zlib1g-dev \
    libcairo2 \
    libpango-1.0-0 \
    libgdk-pixbuf-xlib-2.0-0 \
    libpangocairo-1.0-0 \
    fonts-liberation \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Django static config
ENV STATIC_URL=/static/
ENV STATIC_ROOT=/app/staticfiles

# Copy entrypoint
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
