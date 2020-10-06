import sys
def get(n):
    if n == 0:
        return 0
    else:
        return get(n-1) + n

sys.setrecursionlimit(10000000)
n = int(input())
print(get(n))