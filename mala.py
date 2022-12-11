import math
import os
os.system("pip install termcolor")
from termcolor import colored

class vector:
    def __init__(self,x1,y1,z1,x2,y2,z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
    def magnitude(self):
        return math.sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2)+((self.z2-self.z1)**2))
    def normalize(self):
        length = self.magnitude()
        return [((self.x2-self.x1)/length),((self.y2-self.y1))/length,((self.z2-self.z1))/length]
    def step(self,step):
        [self.normalize()[0]*step,self.normalize()[1]*step,self.normalize()[2]*step]
    
        

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class nearest:
    def point(pointA,pointB):
        return math.sqrt(((pointB.x-pointA.x)**2)+((pointB.y-pointA.y)**2)+((pointB.z-pointA.z)**2))
    def circle(point,centrum,radius):
        return nearest.point(point,centrum)-radius

def calcurate(point,Objects):
    maxdistance = 99999999 #big number
    bestobject = None
    for object in Objects:
        if object[0] == "cirkle":
            distance = nearest.circle(point,object[1],object[2])
            if distance < maxdistance:
                maxdistance = distance
                bestobject = object
    return maxdistance,bestobject

def calcurateray(vector,objects):
    distance = 1
    step = 1
    while distance != 0:
        distance,object = calcurate(point(vector.x1+(vector.normalize()[0])*step,vector.y1+(vector.normalize()[1])*step,vector.z1+(vector.normalize()[2])*step),objects)
        step += distance
        if distance > 1000:
            object = [None]
            break
    if object[0] == None:
        print("Found nothing whit vector: x1: "+str(vector.x1)+" y1: "+str(vector.y1)+" z1: "+str(vector.z1)+" | x2: "+str(vector.x2)+" y2: "+str(vector.y2)+" z2: "+str(vector.z2))
        return
        
    fp = point(vector.x1+(vector.normalize()[0])*step,vector.y1+(vector.normalize()[1])*step,vector.z1+(vector.normalize()[2])*step)

    print("Found "+str(object[0])+ " At: x: "+str(fp.x)+" y: "+str(fp.y)+" z: "+str(fp.z))

os.system("cls")
print("")
print(colored("|---------------------------------|","green"))
print(colored("|  succesfully loaded mala maths  |","green"))
print(colored("|     made by lars! have fun!     |","green"))
print(colored("|---------------------------------|","green"))
print("")
