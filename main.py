from mala import *
import time

def calcurate(point):
    maxdistance = 99999999 #big number
    for object in Objects:
        if object[0] == "cirkle":
            distance = nearest.circle(point,object[1],object[2])
            if distance < maxdistance:
                maxdistance = distance
                bestobject = object
    return maxdistance

def calcurateray(vector):
    distance = 1
    step = 1
    while distance != 0:
        distance = calcurate(point(vector.x1+(vector.normalize()[0])*step,vector.y1+(vector.normalize()[1])*step,vector.z1+(vector.normalize()[2])*step))
        print("----------------")
        print("distance: " + str(distance))
        print("step: " + str(step))
        print("----------------")
        step += distance

CentrumPoint = point(0,0,0)
CentrumPoint2 = point(-12,0,0)
Objects = [["cirkle",CentrumPoint,2],["cirkle",CentrumPoint2,1]]
vec = vector(-10,0,0,-9,0,0)

raycheck(vec)