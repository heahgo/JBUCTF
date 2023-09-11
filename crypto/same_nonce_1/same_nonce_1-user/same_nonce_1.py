from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode

flag = open('/flag', 'rb').read()
key = get_random_bytes(16)
nonce = get_random_bytes(12)
crypto = AES.new(key, AES.MODE_CTR, nonce=nonce)
enc_flag = crypto.encrypt(flag)
enc_flag = b64encode(enc_flag).decode()

for _ in range(5):
    print('[1] encrypt')
    print('[2] flag')
    try:
        n = int(input('>> '))
    except:
        continue
    if n == 1:
        try:
            data = input('data : ')
            data = b64decode(data)
            crypto = AES.new(key, AES.MODE_CTR, nonce=nonce)
            cipher = crypto.encrypt(data)
            cipher = b64encode(cipher).decode()
            print(cipher)
        except:
            continue
    elif n == 2:
        print(enc_flag)
        exit()