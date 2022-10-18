FROM python:3.10.4-slim

WORKDIR /back

RUN apt-get update && \
    apt-get install -y \
    wait-for-it \
    build-essential \
    libpq-dev \
    python3-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /back
