FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json

RUN npm install

COPY . .

# RUN npm run build

EXPOSE 8080

RUN apk update && apk add tzdata
ENV TZ=Europe/Moscow

# CMD ["http-server", "dist"]
CMD ["npm", "run", "serve"]
