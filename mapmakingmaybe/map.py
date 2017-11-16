from PIL import Image
import math
import sys
import random
sys.setrecursionlimit(10000)

def find_start(mapimage):
    for x in range(mapimage.size[0]):
        for y in range(mapimage.size[1]):
            if mapimage.getpixel((x,y)) == (0,0,255):
                return (x,y)
    return None


def find_end(mapimage):
    for x in range(mapimage.size[0]):
        for y in range(mapimage.size[1]):
            if mapimage.getpixel((x,y)) == (255,0,0):
                return (x,y)
    return None
"""
IMG = Image.new("RGB",(800,800),(128,128,128))
"""
global IMG
IMG = Image.open('map1.png')

def kruskal(start,end,maparr):
    print str(start) + str(IMG.getpixel(start))
    try:
        IMG.getpixel(start)
    except IndexError as e:
        #oob
        return False
    if maparr[start[0]][start[1]] == True:
        #already been here
        return False
    else:
        maparr[start[0]][start[1]] = True

    if IMG.getpixel(start) == (0,0,0):
        #Dead end
        return False
    elif start == end:
        print "GOT TO THE END!"
        return 1
    elif IMG.getpixel(start) == (255,255,255) or IMG.getpixel(start) == (0,0,255):

        try:
            if not maparr[start[0]+1][start[1]]:
                run = kruskal((start[0]+1,start[1]),end,maparr)
                if run:
                    IMG.putpixel(start,(0,255,0))
                    print "Put Pixel at " + str(start)
                    return run + 1
        except Exception as e:
            pass

        try:
            if not maparr[start[0]][start[1]+1]:
                run = kruskal((start[0],start[1]+1),end,maparr)
                if run:
                    IMG.putpixel(start,(0,255,0))
                    print "Put Pixel at " + str(start)
                    return run + 1
        except Exception as e:
            pass

        try:
            if not maparr[start[0]-1][start[1]]:
                run = kruskal((start[0]-1,start[1]),end,maparr)
                if run:
                    IMG.putpixel(start,(0,255,0))
                    print "Put Pixel at " + str(start)
                    return run + 1
        except Exception as e:
            pass

        try:
            if not maparr[start[0]][start[1]-1]:
                run = kruskal((start[0],start[1]-1),end,maparr)
                if run:
                    IMG.putpixel(start,(0,255,0))
                    print "Put Pixel at " + str(start)
                    return run + 1
        except Exception as e:
            pass

    else:
        IMG.show()
        return "Could not reach exit"
    raise Exception



maparr = [[None for i in range(20)] for j in range(20)]


start = find_start(IMG)
point = (2,2)

print kruskal(find_start(IMG), find_end(IMG), maparr)
IMG.show()
IMG.save('SolvedMaze.png','PNG')
