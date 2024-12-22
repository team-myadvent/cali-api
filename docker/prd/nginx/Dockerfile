FROM nginx

RUN apk add --no-cache nginx-mod-http-geoip

COPY nginx.conf /etc/nginx/nginx.conf
COPY fullchain.pem /etc/letsencrypt/live/dev.myadvent-calendar.com/fullchain.pem
COPY privkey.pem /etc/letsencrypt/live/dev.myadvent-calendar.com/privkey.pem
