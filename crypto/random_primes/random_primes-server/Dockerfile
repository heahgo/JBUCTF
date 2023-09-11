FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pycryptodome
RUN apt install xinetd -y

COPY ./random_primes.py /root/random_primes.py
COPY ./random_primes /etc/xinetd.d/random_primes
COPY ./flag /flag

RUN echo "random_primes	10007/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]