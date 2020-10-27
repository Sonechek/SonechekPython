import numpy as np
f1 = open('/home/sanek/Рабочий стол/input.txt', 'r')
s  = f1.read()
lst = list(map(int, s.split()))
n = int(len(lst)**.5)
tab = [lst[y*5:y*5+5] for y in range(n)]
a = np.array([tab])
a = a.transpose()
print(a)