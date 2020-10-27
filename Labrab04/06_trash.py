f1 = open('/home/sanek/Рабочий стол/input.txt', 'r')
text  = f1.read()
line = text.split('\n')
lines = text.split()
lines_vt = lines[::-1]
n = len(line)
acc = 0
bat = 0
# for i in range (n):
#     acc +=                      #Здесь мы будем добавлять i-ый элемент n-ой строки в аккумилирующую переменную
#     bat +=                      #А здесь мы будем добавлять i[::-1]-ый элемент n[::-1]-ой строки в акк переменную
#     i += n
i = 0
while i < n:
    acc += line[i]
    bat += line(n-i-1)
    i += 1
print(acc)
print(bat)
# print(lines)
# print(lines_vt)
print(acc, bat)
f1.close()  