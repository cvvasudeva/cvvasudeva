#specify a base image
FROM node:alpine

#install some dependencies
WORKDIR /usr/app
COPY ./ ./
RUN npm install

#Default command
CMD ["npm", "start"]


