FROM alpine:3.8 as builder
MAINTAINER Github: stroebs

WORKDIR /app

COPY app/ /app

RUN apk add --update \
    python \
    py-pip && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -t /app/ -r requirements.txt

FROM alpine:3.8

EXPOSE 8080

WORKDIR /app

RUN apk add --update python && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/*

COPY --from=builder /app /app

CMD ["/app/swarm-meta.py"]
