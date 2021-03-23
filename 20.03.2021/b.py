n, k = input().split()
a = 0
b = 0
n = int(n) # килограмм мяса
k = int(k) # задержка броска
a += (n - k)
b += (n - a)
if a > k or a <= 0:
    a = n // 2
    b = n - a

print(a,b) # размеры кусков мяса