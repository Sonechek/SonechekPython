n = int(input())
a = str('X')
b = str('-')
for i in range(n):
    if i % 2 == 1:
        print(n*(a+b)[:-1])
    else:
        print(n*(b+a)[:-1])