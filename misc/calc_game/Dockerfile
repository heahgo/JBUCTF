FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install xinetd -y

COPY ./calc_game.py /root/calc_game.py
COPY ./calc_game /etc/xinetd.d/calc_game
COPY ./flag /flag

RUN echo "calc_game	10004/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]
