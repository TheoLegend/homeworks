import math

class Geometry: pass

class Circle(Geometry):
    def __init__(self,r): self.r=r
    def area(self): return math.pi*self.r**2
    def perimeter(self): return 2*math.pi*self.r

class Rectangle(Geometry):
    def __init__(self,w,h): self.w,self.h=w,h
    def area(self): return self.w*self.h
    def perimeter(self): return 2*(self.w+self.h)

class Triangle(Geometry):
    def __init__(self,a,b,c): self.a,self.b,self.c=a,b,c
    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self): return self.a+self.b+self.c

for s in [Circle(5),Rectangle(4,6),Triangle(3,4,5)]:
    print(type(s).__name__,round(s.area(),2),round(s.perimeter(),2))
