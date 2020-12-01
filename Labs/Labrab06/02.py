a = list(input())
neiz = 0
if a[1] == '-':
    if a[0] == 'x':
        neiz = int(a[4]) + int(a[2])
    elif a[2] == 'x':
        neiz = int(a[0]) - int(a[4])
    elif a[4] == 'x':
        neiz = int(a[0]) - int(a[2])
if a[1] == '+':
    if a[0] == 'x':
        neiz = int(a[4]) - int(a[2])
    elif a[2] == 'x':
        neiz = int(a[4]) - int(a[0])
    elif a[4] == 'x':
        neiz = int(a[0]) + int(a[2])
print(neiz)