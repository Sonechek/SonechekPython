f1 = open('/home/sanek/Рабочий стол/input.txt', 'r')
text  = f1.read()
lines = text.split('\n')
n = len(lines)
print(n)
for i in range(n):
    if i % 2 == 0:
        print(lines[i])
f1.close()