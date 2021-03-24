from ascii_art_fucntions import get_image_resize, get_image_symbols, inverting_pic_sides
from PIL import Image

print('Желаете отразить картинку?')
while True:
    inverting_ch = int(input('1 - НЕТ!!!!\n'
                             '2 - Хочу вверх ногами!\n'
                             '3 - Только отзеркалить\n'
                             '4 - Я заказываю солянку\n'))
    break
print('Желаете инвертировать цвет?')
while True:
    switching_ch = int(input('1 - Хочу, хочу!!!\n'
                             '2 - Нет, конечно же...\n'))
    break

name_image = '/home/sonechek/Рабочий стол/SonechekPython/Labs/Semestr_2/Labrab5/ascii-art.jpg' 
img = Image.open(name_image)
img_new = get_image_resize(img, 100)