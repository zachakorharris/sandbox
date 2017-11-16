from PIL import Image
import math
import random

img = Image.new("RGB",(1600,1600),(128,128,128))
print random.randint(1,10)
try:

    w = 15
    h = 1600
    n = h/w-1
    start = 0
    for count in range(n):
        start = start + w
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        w = random.randint(5,25)
        for width in range(w):
            for height in range(h):
                img.putpixel((width + start,height),(r,g,b))
                """
        for x in range(25):
            print "x = " + str(x)
            for y in range(25):
                for z in range(25):
                    for h in range(400):
                        print "putting pixel at (" + str(l) + "," + str(h) + ")"
                        img.putpixel((l,h),(10*x,10*y,10*z))

                    l = l + 1
        print count
        print math.sqrt(count)
    """
except Exception as e:
    print e


img.save("rainbow_barcode.png","PNG")

img.show()











"""
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
"""
