n = int(input())
lst = []
a = 1
for i in range(n):
    for i in range(n):
        lst.append(a)
        a += 1
    if a % 2 == 0:
        print(", ".join(repr(e) for e in lst[:n]))
    else:
        print(", ".join(repr(e) for e in lst[:n][::-1]))
    lst.clear()