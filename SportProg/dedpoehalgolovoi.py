x, y, z, w = map(int,input().split())

count = 0
for a in range(100):
    for b in range(100):
        for c in range(100):
            if a*x + b*y + c*z == w:
                count += 1
print(count)