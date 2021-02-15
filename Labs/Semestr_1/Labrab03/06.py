n = int(input())
a = str('X')
b = str('-')
for i in range(n):
    lst = list((i*b)+(a)+((n-i-1)*b))
    print(*lst[::-1])