from random import randint

def run_game():
    wins = 0
    while wins != 5:
        mod = randint(50, 100)
        value = mod * randint(100, 200) + 1
        count = 0
        print(f'Baskin Robbins {value} !!!')

        while count != value:
            while True:
                try:
                    num = list(map(int, input(f'Input Numbers {count + 1} ~ {mod - 1} (ex {count + 1}, {count + 2}, {count + 3} .... {count + mod - 1}) : ').split(', ')))
                    if len(num) >= mod:
                        raise ValueError
                    for i in range(len(num)):
                        if num[i] != count + i + 1:
                            raise ValueError
                except (ValueError, IndexError):
                    print("Retry")
                    continue
                except Exception as e:
                    print(e)
                    exit()
                break
                    
            count += len(num)
            if count == value:
                print("Lose :(")
                exit()

            if value - count < mod - 1:
                bot_num = [i + count + 1 for i in range(randint(1, value - count))]
            else:
                bot_num = [i + count + 1 for i in range(randint(1, mod - 1))]
            
            count += len(bot_num)

            print('YOU : ' + ', '.join(map(str, num)))
            print("BOT : " + ', '.join(map(str, bot_num)))

            if count == value:
                print("Win :)")
                wins += 1
                break
    print(f'flag : {flag}')

if __name__ == '__main__':
    flag = open('/flag', 'r').read()
    run_game()