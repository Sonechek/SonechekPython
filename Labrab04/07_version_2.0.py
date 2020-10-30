f1 = open('/home/sanek/Рабочий стол/input.txt', 'r')
s  = f1.read()
lst = list(map(int, s.split()))
n = int(len(lst)**.5)
# в идеале найти кол-во элементов в столбике и записать в m
matrix = [lst[y*5:y*5+5] for y in range(n)]

result = []
for i in range(n):
    tmp = []
    for k in range(n):
        tmp = tmp + [matrix[k][i]]
    result = result + [tmp]

print(result)
f1.close