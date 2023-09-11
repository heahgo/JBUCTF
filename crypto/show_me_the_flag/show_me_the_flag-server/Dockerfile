FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pycryptodome
RUN apt install xinetd -y

COPY ./show_me_the_flag.py /root/show_me_the_flag.py
COPY ./show_me_the_flag /etc/xinetd.d/show_me_the_flag
COPY ./flag /flag

RUN echo "show_me_the_flag	10001/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]