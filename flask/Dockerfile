FROM python:slim
RUN pip install --no-cache flask gunicorn 
COPY src /src
EXPOSE 5000
WORKDIR /src
ENTRYPOINT ["gunicorn", "-c", "gunicorn_conf.py", "main:app"]
