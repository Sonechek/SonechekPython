from PIL import Image

#switching size of pic
def get_image_resize(img, height_new):
    width, height = img.size
    width_new = width // (height//height_new)
    img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_new

name_image = '/home/sonechek/Рабочий стол/SonechekPython/Labs/Semestr_2/Labrab5/ascii-art.jpg' 
img = Image.open(name_image)
img_new = get_image_resize(img, 100)

symbols = ' &?!$*#'

result = ''

#getting pic symbols
def get_image_symbols():
    count = len(symbols)
    full = 256 + 256 + 256
    segment = full // count
    
    width, height = img_new.size
    for y in range(height):
        for x in range(width):
            r, g, b = img_new.getpixel((x, y))
            color = r + g + b
            pos = color // segment
            result += symbols[pos] * 2
        result += '\n'
    return result


#inverting sides of pic





#switching color of pic



    

#writing result in file
f1 = open('output-ascii.txt', 'w')
f1.write(result)
f1.close()
