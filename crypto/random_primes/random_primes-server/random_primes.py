from Crypto.Util.number import getPrime
from random import randint

flag = open('/flag', 'rb').read()
flag = int.from_bytes(flag, 'big')

def gen_prime_list(n):
    primes = []
    for i in range(n):
        primes.append(getPrime(512))
    return primes

primes = gen_prime_list(4)

e = 65537
p = primes[randint(0, len(primes) - 1)]
q = primes[randint(0, len(primes) - 1)]
n = p * q

c = pow(flag, e, n)
primes = ', '.join(map(str, primes))
print(f'enc_flag = {c}')
print(f'primes = [{primes}]')

