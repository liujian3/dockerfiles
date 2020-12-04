FROM node:10.16.0
ENV ADDR=127.0.0.1:8081
RUN npm config set user-agent "npm/6.9.0 node/v10.16.0 win32 x64"
RUN npm config set registry http://${ADDR}/repository/npm-proxy/
RUN npm install yarn -g
RUN yarn config set user-agent "yarn/1.22.10 npm/? node/v10.16.0 win32 x64"
RUN yarn config set registry http://${ADDR}/repository/npm-proxy/
