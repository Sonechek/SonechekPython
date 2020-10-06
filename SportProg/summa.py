n = int(input())
# print(sum(range(1,n+1)))
if 0 < n <= 10**4:
    sum = (n+1)*n // 2
else:
    sum = (n-1)*n // 2 * (-1) + 1
print(sum)