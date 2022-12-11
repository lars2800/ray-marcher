import math

class vector:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def magnitude(self):
        return math.sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2))
    def normalize(self):
        length = self.magnitude()
        return [((self.x2-self.x1)/length),((self.y2-self.y1))/length]

vec1 = vector(0,5,0,10)
print(vec1.normalize())
print(vec1.magnitude())