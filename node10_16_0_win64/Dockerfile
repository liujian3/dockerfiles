FROM node:10.16.0
ENV ADDR 127.0.0.1:8081
RUN npm install yarn -g
COPY ./config.sh /config.sh
ENTRYPOINT ["/bin/bash","/config.sh"]
