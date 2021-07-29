FROM python:3.9-slim
WORKDIR /app

RUN apt-get update && \ 
  apt-get install -y git && \
  pip3 install -U git+https://github.com/Gerapy/Gerapy.git && \
  pip3 install scrapy && \
  apt-get remove -y git

COPY ./run.sh /app/run.sh
RUN chmod a+x /app/run.sh
VOLUME /app/gerapy
CMD /bin/bash /app/run.sh
