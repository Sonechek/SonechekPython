f1 = open('/home/sanek/Рабочий стол/input.txt', 'r')
s  = f1.read()
lst = list(map(int, s.split()))
n = int(len(lst)**.5)
tab = [lst[y*5:y*5+5] for y in range(n)]

#  acc = 0
# for y in range(n):
# 	for x in range(n):
# 		if x == y:
# 			acc += tab[y][x]
# print(acc)


acc = 0
for i in range(n):
	acc += tab[i][i]
print(acc)

bat = 0
y = n - 1
x = 0
for i in range(n):
	bat += tab[y][x]
	y -= 1
	x += 1 
print(bat)

f1.close()  