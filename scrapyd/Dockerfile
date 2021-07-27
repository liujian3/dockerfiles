FROM python:3.9-slim
WORKDIR /app
COPY . /app
COPY ./scrapyd.conf /etc/scrapyd/
RUN pip install pip -U \
    && pip install -r requirements.txt
EXPOSE 6800
CMD ["scrapyd"]
