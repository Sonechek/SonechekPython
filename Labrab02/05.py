import math
x = int(input())
n = int(input())
sum_1 = 0
for i in range(n):
    if i % 2 == 0:
        sum_1 = sum_1 +(x**(n+2))/(math.factorial(n+2))
    else:
        sum_1 = sum_1 + (x**(n+2))/(math.factorial(n+2))
print("%.3f" % sum_1 )