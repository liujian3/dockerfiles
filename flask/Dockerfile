FROM python:3.9
RUN pip install --no-cache flask gunicorn 
COPY src /src
EXPOSE 5000
WORKDIR /src
ENTRYPOINT ["gunicorn", "-w", "4"]
