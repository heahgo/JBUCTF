from Crypto.Util.number import getPrime, isPrime
from random import randrange

flag = open('/flag', 'rb').read()
m = int.from_bytes(flag, 'big')

r = randrange(2**15, 2**16) 

p = getPrime(1024)
q = p + r * 2
while isPrime(q) != True:
    q += 2
e = 0x10001
n = p * q

c = pow(m, e, n)

print(f'{c=}')
print(f'{n=}')
print(f'{e=}')
