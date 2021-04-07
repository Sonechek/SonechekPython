from PIL import Image
from functions_for_sifr import get_alph


def de_cifr(image_name, alph):
    img = Image.open(image_name)
    rastr = img.load()
    x, y = 0, 0
    stroka = ''
    while True:
        pos_b = ''
        for p in range(3):
            (r, g, b) = rastr[x, y]
            pos_b += str(r & 1)
            pos_b += str(g & 1)
            pos_b += str(b & 1)
            x += 1
        # pos = pos_b[:-1]
        pos = int(pos_b[::-1], 2)
        simv = alph[pos]
        if simv == '~':
            stroka += '\n'
        elif simv == '^':
            break
        else:
            stroka += simv

        with open('output_decifr.txt', mode='w', encoding='utf8') as w:
            w.write(stroka)


alph = get_alph()
image_name = '1_bladerunner.bmp'

de_cifr(image_name, alph)
