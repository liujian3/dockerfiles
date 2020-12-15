FROM python:3.8
RUN pip install flask uwsgi
COPY src /src/
EXPOSE 5000
ENTRYPOINT ["python", "/src/app.py"]
