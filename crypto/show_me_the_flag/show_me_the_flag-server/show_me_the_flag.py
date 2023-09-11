from Crypto.Util.number import getPrime

flag = open('/flag', 'rb').read()

p , q = getPrime(1024), getPrime(1024)
n = p * q
n_1 = n - 1
phi = (p - 1) * (q - 1)
e = 0x10001
d = pow(e, -1, phi)

print(f'{n=}')
print(f'{e=}')

try:
    data1 = int(input('Input data1 : '))
    data2 = int(input('Input data2 : '))
    if  data1 < 2**1024 or data1 >= 2**2048:
        raise ValueError
    if  data2 < 2**1024 or data2 >= 2**2048:
        raise ValueError
except ValueError:
    print('Value Error')
    exit()
except Exception as e:
    print(e)
    exit()
    
enc1, enc2 = pow(data1, d, n), pow(data2, e, n)

if int(b'show_me_the_flag'.hex(), 16) == (enc1 * enc2) % n:    
    print(f'flag : {flag.decode()}')
else:
    print('Falied')
    
