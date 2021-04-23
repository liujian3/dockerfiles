FROM python:3.9
RUN pip install --no-cache flask gunicorn 
COPY src /src
EXPOSE 5000
WORKDIR /src
ENTRYPOINT ["uwsgi", "--http", "127.0.0.1:5000", "--module", "main:app"]
