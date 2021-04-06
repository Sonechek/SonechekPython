from PIL import Image
from functions_for_sifr import get_alph


def de_cifr(alph, img):
    x, y = 0, 0
    shift = 0
    pos_b = ''
    for p in range(3):
        (r, g, b) = rastr(x, y)
        pos_b += str(r & 1); shift +=1
        pos_b += str(g & 1); shift +=1
        pos_b += str(b & 1); shift +=1
        x += 1
    pos = int(pos_b[::-1], 2)




    return text


alph = get_alph()
image_name = '1_draiv.jpg'
img = Image.open(image_name)
rastr = img.load()


de_cifr()
print(pos)