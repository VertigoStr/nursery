FROM nginx:stable-alpine

RUN mkdir /srv/media

COPY conf.d/ /etc/nginx/conf.d
COPY certs/ /etc/nginx/certs
COPY run.sh /run.sh

ENTRYPOINT []
CMD /run.sh
