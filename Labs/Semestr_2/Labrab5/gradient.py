from PIL import Image

img = Image.open(r'''/home/sonechek/Рабочий стол/SonechekPython/Labs/Semestr_2/Labrab5/1-removebg-preview.jpg''')

width, height = img.size

kx = 256 / width
ky = 256 / height

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x,y))
        if r == 158 and g == 158 and b == 158:

            clr = int((kx * y)/2)
        
            r, g, b = clr, clr, clr
            img.putpixel((x, y), (r, g, b))

img.show()
