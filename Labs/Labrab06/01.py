n = list(map(int, input().split()))
maximum = max(n)
minimum = min(n)
proc = (minimum/maximum)*100
print(round(proc))