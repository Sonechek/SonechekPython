f1 = open('/home/sanek/Рабочий стол/input.txt', 'r')
text  = f1.read()
lines = text.split('\n')
acc = 0
n = len(lines) 
for i in range(n-1):
        if sum(list(map(int, lines[i].split(' ')))) > sum(list(map(int, lines[i+1].split(' ')))):
            acc = lines[i]
print(acc)
f1.close()