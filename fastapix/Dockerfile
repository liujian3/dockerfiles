  
ENV PYTHON_VERSION=3.9
FROM python:$PYTHON_VERSION-slim

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn pandas ldap3 fastapi cx_Oracle authlib asyncpg aioredis redis requests sqlalchemy aiofiles httpx itsdangerous jinja2 xlrd openpyxl pymysql

COPY ./start.sh /start.sh
COPY ./ljpath.pth /usr/local/lib/python$PYTHON_VERSION/site-packages/ljpath.pth
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]
