'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

from math import pi

class Rect:
    '''Define a rectangle and set methods to determine its properties'''

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f"Rectangle with length {self.length} and width {self.width}."

    def __str__(self):
        return f"This rectangle is {self.length} units long and {self.width} units wide."

    def area(self):
        '''Calculate and return the area of the rectangle'''
        a = self.length * self.width
        return a

    def perim(self):
        '''Calculated and return the perimeter of the rectangle'''
        p = 2 * (self.length + self.width)
        return p
    
class Circle:
    '''Define a circle and set methods to determine its properties'''

    def __init__(self,radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle with radius {self.radius}."

    def __str__(self):
        return f"This circle has a radius of {self.radius} units."

    def area(self):
        '''Calculate and return the area of the circle'''
        a = pi * (self.radius**2)
        return a

    def circum(self):
        '''Calculated and return the circumference of the circle'''
        c = pi * self.radius * 2
        return c

#for testing:
r = Rect(3,5)
print(r)
print(f"area: {r.area()} | perimeter: {r.perim()}")
c = Circle(4)
print(c)
print(f"area: {c.area()} | circumference: {c.circum()}")

