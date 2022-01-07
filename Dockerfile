FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update -y && \
    apt-get upgrade && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "python3", "bot.py" ]
