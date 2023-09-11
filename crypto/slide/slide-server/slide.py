from myCrypto import *
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode

flag = open('/flag', 'rb').read()
key = get_random_bytes(16)
crypto = myCrypto(key)
enc_flag = crypto.encrypt(pad(flag, 16))

for i in range(10):
    print('encrypt [1]')
    print('slide   [2]')
    print('flag    [3]')
    print('exit    [4]')
    try:
        i = int(input('>> '))
        if i < 1 or i > 4:
            raise ValueError
    except Exception as e:
        print(e)
        exit()
    if i == 1:
        try:
            p = b64decode(input('Input text (base64) >> '))
            print(b64encode(crypto.encrypt(pad(p, crypto.block_size))).decode())
        except Exception as e:
            print(e)
            exit()
    elif i == 2:
        try:
            p = b64decode(input('Input text (base64) >> '))
            p = pad(p, crypto.block_size)
            states = [p[i: i+16] for i in range(0, len(p), crypto.block_size)]
            result = b''
            for state in states:
                state = byte2state(state)   
                state = crypto.round(state)
                result += state2byte(state)
            print(b64encode(result).decode())
        except Exception as e:
            print(e)
            exit() 
    elif i == 3:
        print(b64encode(enc_flag).decode())
    elif i == 4:
        exit()