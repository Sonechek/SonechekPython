from PIL import Image

img = Image.open('/home/sonechek/Рабочий стол/SonechekPython/Labs/Semestr_2/Labrab3/1.jpg')
width, height = img.size

kx = 256 / width 
ky = 256 / height 

for y in range(height):
    for x in range(width):
        clr = int(kx * x)
        r, g, b = clr, clr, clr
        img.putpixel((x, y), (r, g, b))

img.show()
img.show()