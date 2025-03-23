From node:22 AS vuebuilder
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./frontend/
RUN cd frontend && npm run build

FROM nginx:alpine AS nginx
COPY --from=vuebuilder /app/frontend/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

FROM python:3.12-slim AS fastapibuilder
WORKDIR /app
COPY server/requirements.txt ./
RUN pip install -r requirements.txt
COPY server/ ./server/