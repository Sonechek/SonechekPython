n = int(input())
a = str('X')
b = str('-')
for i in range(n):
    if i % 2 == 0:
        print(a*n)
    else:
        print(b*n)
