from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from random import randint
from base64 import b64encode, b64decode

flag = open('/flag', 'rb').read()

secret = get_random_bytes(randint(33, 48))
key, nonce = get_random_bytes(16), get_random_bytes(12)
crypto = AES.new(key, AES.MODE_GCM, nonce=nonce)
enc_secret, secret_tag = crypto.encrypt_and_digest(secret)
enc_secret = b64encode(enc_secret).decode()
p1, p2 = get_random_bytes(randint(17, 32)), get_random_bytes(randint(17, 32))

ciphers = []
for p in [p1, p2]:
    crypto = AES.new(key, AES.MODE_GCM, nonce=nonce)
    c, t = crypto.encrypt_and_digest(p)
    c = b64encode(c+t).decode()
    ciphers.append(c)


for i in range(10):
    print('[1] show_ciphers')
    print('[2] show_secret')
    print('[3] verify')
    print('[4] exit')

    try:
        n = int(input('>> '))
        if n < 1 or n > 4:
            raise ValueError
    except:
        print('Retry')
        continue
    if n == 1:
        print(f'c1 : {ciphers[0]}')
        print(f'c2 : {ciphers[1]}') 
        continue
    if n == 2:
        print(f'enc_secret : {enc_secret}')
        continue
    if n == 3:
        try:
            edata = input('edata : ')
            edata = b64decode(edata)
            cipher = edata[:-16]
            tag = edata[-16:]
            crypto = AES.new(key, AES.MODE_GCM, nonce=nonce)
            result = crypto.decrypt_and_verify(cipher, tag)
        except:
            print('Failed')
            continue
        if result == secret:
            print(f'flag : {flag.decode()}')
            exit()
    if n == 4:
        exit()

