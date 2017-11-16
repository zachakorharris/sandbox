from PIL import Image
import math
import random

img = Image.new("RGB",(1600,1600),(128,128,128))

COLORSdict = {
    'RED': (255,0,0),
    'BLUE': (0,0,255),
    'YELLOW': (255,255,0),
    'GREEN': (0,255,0),
    'ORANGE': (0,255,255),
    'PURPLE': (255,0,255)
    }

COLORS = [
    (255,0,0),
    (0,0,255),
    (255,255,0),
    (0,255,0),
    (0,255,255),
    (255,0,255)
]

def sign(p1, p2, p3):
    return (((p1[0] - p3[0]) * (p2[1] - p3[1])) - ((p2[0] - p3[0]) * (p1[1] - p3[1])))
try:
    pointA = (200,200)
    pointB = (200,300)
    pointC = (300,300)
    pt = (250,220)

    print sign(pt,pointA,pointB)
    print sign(pt,pointB,pointC)
    print sign(pt,pointC,pointA)
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


img.save("polkadots_6colors.png","PNG")

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
