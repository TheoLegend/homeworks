import math

class Shape:
    def area(self): return 0
    def perimeter(self): return 0

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r**2
    def perimeter(self): return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(type(s).__name__, "Area:", round(s.area(), 2), "Perimeter:", round(s.perimeter(), 2))
