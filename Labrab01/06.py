import math
a = int(input('Введите корень a -'))
b = int(input('Введите корень b -'))
c = int(input('Введите корень c -'))

if diskr > 0:
diskr = b ** 2 - 4 * a * c
korn_1 = (-b + math.sqrt(diskr)) / (2 * a)
korn_2 = (-b - math.sqrt(diskr)) / (2 * a)
print('Первый корень - ', korn_1, 'Второй корень - ', korn_2)
elif diskr == 0:
    korn_3 = -b / (2 * a)
    print ('Корень при дискриминанте равном 0', korn_3)
else:
    print('Корней нет')