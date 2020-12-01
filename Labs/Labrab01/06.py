import math
a = int(input('Введите первую неизвестную - '))
b = int(input('Введите вторую неизвестную - '))
c = int(input('Введите третью неизвестную - '))

diskr = (b ** 2) - (4 * a * c )
if diskr > 0:
  kor_1 = ( -b + math.sqrt(diskr)) / (2 * a)
  kor_2 = ( -b - math.sqrt(diskr)) / (2 * a)
  print ('Первый корень ', kor_1, 'Второй корень ', kor_2, sep = '\n')

elif diskr == 0:
  kor_3 = (-b) / (2 * a)
  print('Корень при дискриминанте равном 0', kor_3)
else:
	print('Корней нет')
  