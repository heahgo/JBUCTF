FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pycryptodome
RUN apt install xinetd -y

COPY ./same_nonce_1.py /root/same_nonce_1.py
COPY ./same_nonce_1 /etc/xinetd.d/same_nonce_1
COPY ./flag /flag

RUN echo "same_nonce_1	10005/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]