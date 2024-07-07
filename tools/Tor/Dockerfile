FROM ubuntu:20.04

RUN apt update
RUN apt install tor -y
RUN apt install curl -y

COPY torrc /etc/tor/
RUN chmod 644 /etc/tor/torrc

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["tail", "-f", "/dev/null"]