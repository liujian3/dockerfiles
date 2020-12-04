FROM node:10.16.0

RUN npm install yarn -g
RUN npm config set user-agent "npm/6.9.0 node/v10.16.0 win32 x64"
RUN yarn config set user-agent "yarn/1.22.10 npm/? node/v10.16.0 win32 x64"
RUN npm config set registry http://127.0.0.1.:8081/repository/npm-proxy/
RUN yarn config set registry http://127.0.0.1.:8081/repository/npm-proxy/
