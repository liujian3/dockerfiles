FROM python:3.8
RUN pip install flask uwsgi
COPY src /src
EXPOSE 5000
WORKDIR /src
ENTRYPOINT ["uwsgi", "--http", "127.0.0.1:5000", "--module", "main:app"]
