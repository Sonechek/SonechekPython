n = int(input())
summ = 0
count = 0
if n == 0:
    summ = 1
if n > 0:
    for i in range(1,n + 1):
        summ += i
if n < 0:
    summ = 1
    while count != abs(n) + 1:
        summ += count * -1
        count += 1
print(summ)