FROM node:22 AS vuebuilder
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .

FROM vuebuilder AS vuebuilderprod
COPY --from=vuebuilder package*.json ./
RUN npm run build

FROM nginx:alpine AS nginx
COPY --from=vuebuilderprod /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

FROM python:3.12-slim AS fastapibuilder
WORKDIR /app
COPY server/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY server/ ./server/