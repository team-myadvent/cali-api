FROM nginx

RUN apt-get update && \
    apt-get install -y nginx-module-geoip

COPY nginx.conf /etc/nginx/nginx.conf
COPY fullchain.pem /etc/letsencrypt/live/dev.myadvent-calendar.com/fullchain.pem
COPY privkey.pem /etc/letsencrypt/live/dev.myadvent-calendar.com/privkey.pem
