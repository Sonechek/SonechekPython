k = int(input())
i = 1
summa = 0
while i * i < k + 1:
    if not k%i:
        summa += 1
    i += 1
print(summa)