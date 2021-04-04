##
# Build container
##

FROM python:3.8-buster AS builder

RUN apt update
RUN apt install -y git
RUN apt install -y build-essential

WORKDIR /work
COPY requirements.txt /work

RUN pip install -r /work/requirements.txt
# todo) static version
RUN pip install wheel uwsgi

##
# Exec container
##

FROM python:3.8-slim

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi
COPY --from=builder /work/src /work/src

RUN apt update \
  && apt install -y libpq5 libxml2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY web/ uwsgi.ini /app

RUN useradd -r -s /bin/false uwsgi-user
RUN chown -R uwsgi-user /app

EXPOSE 5000
USER uwsgi-user
CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
