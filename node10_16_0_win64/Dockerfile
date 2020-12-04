FROM node:10.16.0
ARG ADDRX=127.0.0.1:8081
ENV ADDR=$ADDRX
RUN npm install yarn -g
COPY ./config.sh /config.sh
CMD ["/bin/bash","/config.sh"]
