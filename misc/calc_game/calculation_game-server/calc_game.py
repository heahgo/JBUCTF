from random import randint
from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

def calc(coef, soul):
    result = 0
    for i in range(len(soul)):
         result += coef[i] * soul[i]
    return result

def swap(soul, i, j):
    soul[i] ^= soul[j]
    soul[j] ^= soul[i]
    soul[i] ^= soul[j]
    return soul

def printEqua(coef, soul):
    for i in range(len(soul)):
        if i == len(soul) - 1:
            print(f'({coef[i]} * {soul[i]}) = {calc(coef, soul)}')
            break
        print(f'({coef[i]} * {soul[i]})', end=' + ')
    print(f'The constant term is {calc(coef, soul)}.')

def initEqua():
    soul, coef = [0] * 5, [0] * 5
    const = randint(-15, 15)

    for i in range(len(soul)):
        soul[i] = randint(-30, 30)
        coef[i] = randint(-10, 10)
    return soul, coef, const        

@timeout(5, '\n\nTIME OUT')
def run_game(soul, coef, const):
    for r in range(5):
        printEqua(coef, soul)
        print(f'The constant term we need is {const}. \n')

        while True:
            print(f'swap count : {5 - r}')
            try:
                i, j = map(int, input('Input index to swap (ex 1 3) : ').split())
                if i < 0 or i > 4 or j < 0 or j > 4:
                    raise IndexError
            except (IndexError, ValueError):
                print('Retry')
                continue
            except Exception as e:
                print(e)
                exit()
            break

        soul = swap(soul, i, j)  

        if calc(coef, soul) == const:
            print(f'Flag is : {flag.decode()}')
            exit()

    print()
    printEqua(coef, soul)
    print('\nFailed :(')

if __name__ == '__main__':
    flag = open('/flag', 'rb').read()
    soul, coef, const = initEqua()
    run_game(soul, coef, const)


