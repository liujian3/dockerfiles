from node

ENV ACCEPT_HIGHCHARTS_LICENSE="YES"

RUN npm install highcharts-export-server -g 

WORKDIR /usr/local/lib/node_modules/highcharts-export-server/
RUN npm install inkscape xmlhttprequest

RUN apt-get update && apt-get install -yq --no-install-recommends \
    inkscape
    
WORKDIR /

EXPOSE 8080
ENTRYPOINT ["highcharts-export-server", "--enableServer", "1", "--port", "8080","--workers","10","--logDest","."]
