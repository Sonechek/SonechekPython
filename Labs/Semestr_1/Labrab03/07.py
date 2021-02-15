n = int(input())
a = str('X')
b = str('-')
for i in range(n+2):
    if i % 2 == 0:
        print((n*(a+b))[:-1])
    else:
        print((n*(b+a))[:-1])