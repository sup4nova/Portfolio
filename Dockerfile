FROM node:22-alpine AS frontend-builder
WORKDIR /app/front
COPY front/package.json front/package-lock.json* ./
RUN npm ci
COPY front/ .
RUN npm run build

FROM python:3.12-slim
RUN apt-get update && apt-get install -y nginx supervisor ...
# installe back, copie le dist du front, lance les deux