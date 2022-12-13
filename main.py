from mala import *
from termcolor import colored as addcolor
import time
from threading import Thread

CentrumPoint = point(5,5,0)

Objects = [["cirkle",CentrumPoint,2.5]]
vec = vector(-10,0,0,-9,0,0)

img = CreateImage(10,10)
img.save()

for y in range(0,10):
    for x in range(0,10):
        vec = vector(0,0,-40,x,y,0)
        if calcurateray(vec,Objects)[0] == "cirkle":
            img.set_pixel(x,y,(255,0,0))
            img.save()
            print("x: "+str(x) +" y: "+str(y)+"  cirkle loaded!")
img.save()
