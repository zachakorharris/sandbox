from PIL import Image
import math
import random

for i in range (10):
    img = Image.new("RGB",(1600,1600),(0,0,0))
    img.show()
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

    try:
        width = 50
        height = 50
        xcount = 0
        ycount = 0
        while ycount < 1600:


            xcount = 0
            while xcount < 1600:
                color = COLORS[random.randint(0,5)]
                x = color[0]
                y = color[1]
                z = color[2]
                for w in range(width):
                    for h in range(height):
                        img.putpixel((xcount + w,ycount + h),(25*x,25*y,25*z))
                        """print "xcount = " + str(xcount)
                        print "ycount = " + str(ycount)
                        print "w = " + str(w)
                        print "h = " + str(h)"""
                xcount += width
            ycount += height
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


    img.save("polkadots/polkadots_" + str(i) + ".png","PNG")





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
