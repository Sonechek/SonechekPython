n = list(input())
summa_1 = 0
summa_2 = 0
for i in range(len(n)):
    if n[i] == '0':
        summa_1 += 1
    else: 
        if summa_1 > summa_2:
            summa_2 = summa_1
        summa_1 = 0
print(summa_2)