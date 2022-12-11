import math

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

CentrumPoint = point(0,0,0)
VecPoint = point(-10,0,0)
print(nearest.circle(VecPoint,CentrumPoint,1))
