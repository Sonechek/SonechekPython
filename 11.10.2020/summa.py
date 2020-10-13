n = int(input())
acc = 0
for i in range (abs(n+1)):
    if n < 0:
        acc -= i

    else:
        acc += i
print(acc)