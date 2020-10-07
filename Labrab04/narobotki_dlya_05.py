n = input()
b = input()

if sum(map(int, n.split(' '))) > sum(map(int, b.split(' '))):
    acc = n
else:
    acc = b


print(acc)