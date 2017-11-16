from PIL import Image
import math
import random


COLORSdict = {
    'RED': (255,0,0),
    'BLUE': (0,0,255),
    'YELLOW': (255,255,0),
    'GREEN': (0,255,0),
    'ORANGE': (0,255,255),
    'PURPLE': (255,0,255)
    }

SCALEFACTOR = 100
XMAX = 1000
YMAX = 1000
BGCOLOR = (128,128,128)
LINECOLOR = (0,0,255)
MAINLINECOLOR = (255,0,0)
img = Image.new("RGB",(XMAX,YMAX),BGCOLOR)

for x in [x * XMAX/20 for x in range(20)]:
    for y in range(YMAX):
        if x == XMAX/2:
            img.putpixel((x,y),MAINLINECOLOR)
        else:
            img.putpixel((x,y),LINECOLOR)


for y in [y * YMAX/20 for y in range(20)]:
    for x in range(XMAX):
        if y == YMAX/2:
            img.putpixel((x,y),MAINLINECOLOR)
        else:
            img.putpixel((x,y),LINECOLOR)



try:
    for x in range(XMAX):
        for y in range(YMAX):
            if math.fabs((x-500)*(x-500)*(x-500) - (y-500)) < 20:
                img.putpixel((x,y),COLORSdict['BLUE'])
except Exception as e:
    pass







img.show()

"""test = [1,2,3]
print [x * 2 for x in test]"""
