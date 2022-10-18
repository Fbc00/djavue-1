FROM python:3.10.4-slim

WORKDIR /backend

RUN apt-get update && \
    apt-get install -y \
    wget \
    net-tools \
    build-essential \
    libpq-dev \
    python3-dev

COPY requirements.txt /backend/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend/
