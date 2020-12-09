lst = list(input())
n = int(input())
k = 0
b = 0
d = 0
sek = 0
for i in range(len(lst)-2):
    if lst[i] == ":":
        lst.pop(i) # избавляемся от двоеточий
a = list(str(n // 60)) # количество минут в n
c = n - (int(''.join(a))*60) # оставшиеся секунды
if int(''.join(a)) >= 60:
    k = int(''.join(a)) // 60 # количество часов
    b = int(''.join(a)) - (k * 60) # остаток минут
    if len(str(b)) == 1:
        timer = str(k) + str(b) + '0' + str(c) # полное время
    elif len(str(b)) == 0:
        timer = str(k) + '0' + '0' + str(c)
    elif len(str(b)) == 2:
        timer = str(k) + str(b) + str(c)
elif int(c) >= 60:
    d = list(str(c // 60)) # количество минут
    sek = c - (d*60) # остаток секунд
    timer = str(d) + str(k) # полное время
else:
    timer = str(n)
full_timer = int(''.join(lst)) + int(timer)
# timer_lst = list(str(timer))
# while len(timer_lst) != 6:
#     timer_lst.insert(0, 0) # возвращаем формат часов
# timer_lst.insert(2, ':')
# timer_lst.insert(5, ':')
print(d)
print(sek)
print(c) 
# print(timer)
# print(full_timer)