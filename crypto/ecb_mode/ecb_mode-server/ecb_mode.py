from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode

flag = open('/flag', 'rb').read()

BLOCK_SIZE = 16
key = get_random_bytes(16)
crypto = AES.new(key, AES.MODE_ECB)

while True:
    try:
        data = b64decode(input('plain text (base64) >> '))
    except:
        print('Retry')
        continue
    enc_data = crypto.encrypt(pad(data + flag, BLOCK_SIZE))
    print(f'enc_data : {b64encode(enc_data).decode()}')
