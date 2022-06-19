# syntax=docker/dockerfile:1

FROM python:3
WORKDIR /flask
COPY . .
RUN apt-get -y install curl
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y


RUN echo "[SQL Server]\n\
Description = SQL Server Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini


RUN pip3 install -r requirements.txt



CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
