#base image redis alpine images
FROM redis:5.0.3-alpine

#storage
VOLUME /var/lib/redis
