f1 = open('/home/sanek/Рабочий стол/input.txt', 'r')
acc = 0
text  = f1.read()
lines = text.split('\n')
n = len(lines)
for line in lines:
    lst = line.split(' ')
    for i in range(n):
        acc += int(lst[i])
    
    
print (acc)
f1.close()