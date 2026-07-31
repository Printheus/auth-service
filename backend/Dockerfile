FROM docker.arvancloud.ir/python:3.12-slim-bookworm

RUN apt-get update

RUN apt-get install -y --no-install-recommends --no-install-suggests \ 
  python3-dev build-essential default-libmysqlclient-dev pkg-config \ 
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY req.pip ./
RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`

RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`

RUN pip install -r req.pip
COPY . .
CMD [ "python", "runner.py" ]