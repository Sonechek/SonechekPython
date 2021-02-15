a = int(input('Введите число - '))
b_str = ''
while a > 0:
    b = a % 8
    b_str += str(b)
    a //= 8
print ('Число в 8-очной системе - ', b_str[::-1])