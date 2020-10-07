f1 = open('/home/sanek/Рабочий стол/input.txt', 'r')
text  = f1.read()
lines = text.split('\n')
n = len(lines)
f2 = open('/home/sanek/Рабочий стол/output.txt', 'w')
for i in range(n):
    line = str(i+1) + ' ' + lines[i] + '\n'
    f2.write(line)
f1.close()
f2.close()
