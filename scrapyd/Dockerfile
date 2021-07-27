FROM python:3.9-slim
WORKDIR /app
COPY . /app
COPY ./scrapyd.conf /etc/scrapyd/
RUN pip install pip -U \
    && pip install --no-cache scrapyd scrapyd-client
EXPOSE 6800
CMD ["scrapyd"]
