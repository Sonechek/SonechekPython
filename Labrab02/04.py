n = int(input())
sum = 0
a = 2
b = 1
for i in range(n):
    sum += a/b
    if i % 2 == 0:
        b += 2
    else:
        a += 2
print('Сумма n первых членов ряда - ', sum)