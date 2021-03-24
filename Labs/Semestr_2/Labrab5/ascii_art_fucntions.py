from PIL import Image


#switching size of pic
def get_image_resize(img, height_new):
    width, height = img.size
    width_new = width // (height//height_new)
    img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_new


#getting pic symbols
def get_image_symbols():
    width, height = img_new.size
    segment = 256 * 256 * 256 // len(symbols)
    for y in range(height):
        for x in range(width):
            r, g, b = img_new.getpixel((x, y))
            color = r * g * b
            # if switching_ch == 1:
            #     color = abs(255 - r) * abs(255 - g) * abs(255 - b)
            # elif switching_ch == 2:
            #     color = r * g * b
            pos = color // segment
            result += symbols[pos] * 2
        result += '\n'
        pic.append(result)
    


#inverting sides of pic
def inverting_pic_sides():
    with open('outpit_ascii.txt', mode='w', encoding='utf8') as out:
        if inverting_ch == 1:
            for i in range(len(pic)):
                out.write(pic[i])

        if inverting_ch == 2:
            for i in range(len(pic)-1, 0, -1):
                out.write(pic[i])

        if inverting_ch == 3:
            for i in range(len(pic)):
                for k in range(len(pic)-1, 0, -1):
                    out.write(pic[i][k])

        if inverting_ch == 4:
            for i in range(len(pic)-1, 0, 1):
                for k in range(len(pic)-1, 0, -1):
                    out.write(pic[i][k])


name_image = 'ascii_art.jpg'
img = Image.open(name_image)
img_new = get_image_resize(img, 50)

symbols = ' &?#'

result = ''

pic = []
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
print(result)

inverting_pic_sides(get_image_symbols())