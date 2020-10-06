# file = open('INPUT.txt', 'r')
# n = file.read()
# file.close()
n = int(input())
e = '7182818284590452353602875'
if n == 0:
    print(3)
elif n == 25:
    print('2.' + e)
else:
    if e[n] >= '5':
        tmp = e[:n-1] + str(int(e[n-1])+1)
    else:
        tmp = e[:n]
    print('2.' + tmp)
# file = open('OUTPUT.txt', "w")
# file.write(n)
# file.close()