from PIL import Image
import math
import random

img = Image.new("RGB",(800,800),(128,128,128))

for x in range(800):
    for y in range(800):
        img.putpixel((x,y),(x,x-255,x-510))

img.save("grad1.png","PNG")

img.show()

for x in range(800):
    for y in range(800):
        img.putpixel((x,y),(x,x-510,x-255))

img.save("grad2.png","PNG")

img.show()

for x in range(800):
    for y in range(800):
        img.putpixel((x,y),(x-255,x-510,x))

img.save("grad3.png","PNG")

img.show()

for x in range(800):
    for y in range(800):
        img.putpixel((x,y),(x-255,x,x-510))

img.save("grad4.png","PNG")

img.show()


for x in range(800):
    for y in range(800):
        img.putpixel((x,y),(x-510,x,x-255))

img.save("grad5.png","PNG")

img.show()


for x in range(800):
    for y in range(800):
        img.putpixel((x,y),(x-510,x-255,x))

img.save("grad6.png","PNG")

img.show()
