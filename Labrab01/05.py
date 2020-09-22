import math
def dl_okr(r):
    len_okr = 2 * math.pi * r #формула длины окружности
    return len_okr

def pl_kr(r):
    square_kr = math.pi * r ** 2
    return square_kr

r = float(input('Введите радиус круга -'))    
print ('Длина окружности -', dl_okr(r),'Площадь круга -', pl_kr(r), sep = "\n")