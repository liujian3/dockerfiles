FROM python:3.9-slim
WORKDIR /app
COPY . /app
COPY ./scrapyd.conf /etc/scrapyd/
RUN pip install pip -U \
    && pip install --no-cache scrapy==1.8.0 scrapyd scrapyd-client
EXPOSE 6800
CMD ["scrapyd"]
