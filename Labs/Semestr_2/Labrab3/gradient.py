from PIL import Image

img = Image.open('1.bmp')
width, height = img.size

kx = 256 / width 
ky = 256 / height 

for y in range(height):
    for x in range(width):
        clr = int(kx * x)
        r, g, b = clr, clr, clr
        img.putpixel((x, y), (r, g, b))

img.show()