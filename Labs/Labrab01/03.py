num_1 = int(input('Введите первое числое -'))
num_2 = int(input('Введите второе числое -'))
num_3 = int(input('Введите третье числое -'))
num_max = 0
if num_1 > num_2:
    num_max = num_1
else:
    num_max = num_2
if num_2 > num_3 and num_2 > num_max:
    num_max = num_2
else:
     if num_3 > num_max:
         num_max = num_3

print(num_max)