n, k = input().split()
a, b = 0, 0
n = int(n) # килограмм мяса
k = int(k) # задержка броска
a = n - k
b = n - a
if a > k:
    a = n // 2
    b = n - a
if a <= 0:
    a = n // 2
    b = n - a

print(a,b) # размеры кусков мяса
print(n, k)