FROM python:3.8-slim

RUN apt update
RUN apt install -y git
RUN apt install -y curl
COPY . /app
RUN pip install -r /app/requirements.txt

COPY web /var/www/html/web/

ENV PORT 5000
EXPOSE 5000

#コンテナ起動時にFlaskサーバを立ち上げ
CMD ["python", "/var/www/html/web/main.py"]
