FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install xinetd -y

COPY ./baskin_robbins.py /root/baskin_robbins.py
COPY ./baskin_robbins /etc/xinetd.d/baskin_robbins
COPY ./flag /flag

RUN echo "baskin_robbins	10002/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]