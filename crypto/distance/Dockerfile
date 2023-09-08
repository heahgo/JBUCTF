FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pycryptodome
RUN apt install xinetd -y

COPY ./distance.py /root/distance.py
COPY ./distance /etc/xinetd.d/distance
COPY ./flag /flag

RUN echo "distance	10006/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]