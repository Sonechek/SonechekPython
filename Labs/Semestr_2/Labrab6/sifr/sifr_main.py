from PIL import Image
from functions_for_sifr import get_alph, get_bit, get_text


def code(alph, key):
    tabs = text
    with open(f'output.txt', mode='w', encoding='utf8') as w:
        for i in range(len(tabs)):
            line = ''
            for j in range(len(tabs[i])):
                line += alph[(alph.index(tabs[i][j]) + key) % len(alph)]
            w.write(line + '\n')


def cifr_in_pic(alph, name_image, text):
    img = Image.open(name_image)
    width, height = img.size
    rastr = img.load()
    x, y = 0, 0
    i = 0
    while i < len(text):
        smb = text[i]
        pos = alph.find(smb)
        for shift in range(8):
            (r, g, b) = rastr[x, y]
            r = (b & 254) | get_bit(pos, shift)
            g = (b & 254) | get_bit(pos, shift)
            b = (b & 254) | get_bit(pos, shift)
            rastr[x, y] = (r, g, b)
            x += 1
            if x == width:
                x = 0
                y += 1
        i += 1
    img.save('1_' + name_image)
    img.show()


alph = get_alph()
key = 149995388
text = get_text('input.txt')
name_image = 'draiv.jpg'
code(alph, key)
cifr_in_pic(alph, name_image, text)
