FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pycryptodome
RUN apt install xinetd -y

COPY ./slide.py /root/slide.py
COPY ./myCrypto.py /root/myCrypto.py
COPY ./slide /etc/xinetd.d/slide
COPY ./flag /flag

RUN echo "slide	10008/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]