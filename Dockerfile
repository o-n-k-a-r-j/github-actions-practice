
FROM nginx:alpine

COPY day45-site/index.html /usr/share/nginx/html/index.html

EXPOSE 80

