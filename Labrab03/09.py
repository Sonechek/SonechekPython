n = int(input())
lst = []
a = 1
for i in range(n):
    for i in range(n):
        lst.append(a)
        a += 1
        
    print(", ".join(repr(e) for e in lst[:n]))
    lst.clear()