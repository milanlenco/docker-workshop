# My debian image

FROM debian:latest

COPY hello.sh /

RUN chmod u+x hello.sh

USER nobody

ENTRYPOINT ["/hello.sh"]

