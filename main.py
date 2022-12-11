from mala import *
import time


def calcurate(point):
    maxdistance = 99999999 #big number
    bestobject = None
    for object in Objects:
        if object[0] == "cirkle":
            distance = nearest.circle(point,object[1],object[2])
            if distance < maxdistance:
                maxdistance = distance
                bestobject = object
    return maxdistance,bestobject

def calcurateray(vector):
    distance = 1
    step = 1
    while distance != 0:
        distance,object = calcurate(point(vector.x1+(vector.normalize()[0])*step,vector.y1+(vector.normalize()[1])*step,vector.z1+(vector.normalize()[2])*step))
        step += distance
        if distance > 1000:
            object = [None]
            break
    if object[0] == None:
        print("Found nothing whit vector: x1: "+str(vector.x1)+" y1: "+str(vector.y1)+" z1: "+str(vector.z1)+" | x2: "+str(vector.x2)+" y2: "+str(vector.y2)+" z2: "+str(vector.z2))
        return
        
    fp = point(vector.x1+(vector.normalize()[0])*step,vector.y1+(vector.normalize()[1])*step,vector.z1+(vector.normalize()[2])*step)

    print("Found "+str(object[0])+ " At: x: "+str(fp.x)+" y: "+str(fp.y)+" z: "+str(fp.z))


CentrumPoint = point(0,0,0)

Objects = [["cirkle",CentrumPoint,2]]
vec = vector(-10,0,0,-9,0,0)


calcurateray(vec)
