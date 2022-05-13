FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json

COPY . .

RUN npm install


# RUN npm run build

EXPOSE 8080

RUN apk update && apk add tzdata
ENV TZ=Europe/Moscow

# CMD ["npm", "run", "build"]
CMD ["npm", "run", "serve"]
