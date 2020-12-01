n = int(input())
lst = []
for i in range(n):
    lst.append(i+1)
    print(", ".join(repr(e) for e in lst))