FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pycryptodome
RUN apt install xinetd -y

COPY ./ecb_mode.py /root/ecb_mode.py
COPY ./ecb_mode /etc/xinetd.d/ecb_mode
COPY ./flag /flag

RUN echo "ecb_mode	10009/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]