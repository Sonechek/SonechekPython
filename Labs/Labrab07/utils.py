import random

def crazy_teaparty():
    count = 0
    chas = int(st[0:2])
    minutes = int(st[3:5])
    seconds = int(st[6:8])
    seconds += n
    if seconds >= 60:
        while seconds >= 60:
            seconds -= 60
            count += 1
        minutes += count
        count = 0
    if minutes >= 60:
        while minutes >= 60:
            minutes -=60
            count += 1
        chas += count
    ch = str(chas)
    minu = str(minutes)
    sec = str(seconds)
    if len(minu) < 2:
        m = '0' + minu
    if len(sec) < 2:
        s = '0' + sec
    time = ch + ':' + m + ':' + s
    if len(time) == 7:
        time = '0' + time
    print(time)
# st = str(input())
# n = int(input())


def palindroms(palin):
    palin = palin.lower()
    palin = ''.join(c for c in palin if c not in ('!',',',':','.','\n','?',' '))
    if palin == palin[::-1]:
        print('Палиндромчик!')
    else:
        print('Не фартануло!')
    # print(palin)


def cookie_ne_bydet():
    x = random.randint (0,1000)
    y = 1
    count = 10
    while x != y or count != 0:
        y = int(input('Сделай ход - '))
        print('Печенек - ', count)
        if y > x:
            count -= 1
            print('Это много')
        if y < x:
            count -= 1
            print ('Это мало')
        if count == 0:
            print('Повезет в следующий раз')
            break
        if count > 0 and x == y:
            print('Лучший в мире за работой!!!')
            print('Теперь ты можешь съесть', count, 'печенек.')
            break
    
    

# crazy_teaparty()
# palindroms(input())
cookie_ne_bydet()