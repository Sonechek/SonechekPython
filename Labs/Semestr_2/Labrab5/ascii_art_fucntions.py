from PIL import Image



#switching size of pic
def get_image_resize(img, height_new):
    width, height = img.size
    width_new = width // (height//height_new)
    img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_new

symbols = ' &?!$*#░▒▓█'

result = ''
pic = []

#getting pic symbols
def get_image_symbols():
    count = len(symbols)
    full = 256 + 256 + 256
    
    segment = full // count
    
    width, height = img_new.size
    for y in range(height):
        for x in range(width):
            r, g, b = img_new.getpixel((x, y))
            if switching_ch == 1:
                color = r + g + b
            elif switching_ch == 2:
                color = r * g * b
            pos = color // segment
            result += symbols[pos] * 2
        result += '\n'
    pic.append(result)


#inverting sides of pic
def inverting_pic_sides():
    with open('outpit-ascii.txt', mode='w', encoding='utf8') as out:
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

