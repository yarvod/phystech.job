FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install -g @vue/cli

COPY . .

# RUN npm run build

EXPOSE 8080

RUN apk update && apk add tzdata

ENV TZ=Europe/Moscow

# CMD ["http-server", "dist"]
CMD ["npm", "run", "serve"]