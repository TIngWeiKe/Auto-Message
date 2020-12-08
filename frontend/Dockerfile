FROM node:12.16.1

WORKDIR /usr/src/react

COPY ./frontend/package.json ./frontend/yarn.lock ./
RUN yarn install

# Copy Project
COPY frontend /usr/src/react

EXPOSE 3000

CMD yarn install && yarn start
