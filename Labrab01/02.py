num_1 = int(input('Введите первое число - '))
num_2 = int(input('Введите второе число - '))

if num_1 > num_2:
    num_max = num_1
    num_min = num_2
else:
    num_max = num_2
    num_min = num_1

if (num_max % num_min == 0):
    print(num_max, 'кратно', num_min)
else:
    print(num_max, 'не кратно', num_min)