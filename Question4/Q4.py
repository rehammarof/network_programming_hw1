import math

class Point:
    points_count=0
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        Point.points_count+=1

    def print(self):
        print("x=",self.x)
        print("y=",self.y)

    def translate(self,x,y):
        self.x+=x
        self.y+=y

    def distance(self,x=0,y=0):
        return math.sqrt((self.x-x)**2+(self.y-y)**2)

    def print_total():
        print('Total Points:',Point.points_count)


class Circle(Point):
    circles_count=0
    def __init__(self,x=0,y=0,r=1):
        Point.__init__(self,x,y)
        self.r=r
        Circle.circles_count+=1

    def print(self):
        Point.print(self)
        print("r=",self.r)

    def circumference(self):
        return 2*math.pi*self.r

    def area(self):
        return math.pi*(self.r**2)

    def print_total():
        print('Total Circles:',Circle.circles_count)
    
class Cylinder(Circle):
    cylinders_count=0
    def __init__(self,x=0,y=0,r=1,h=10):
        Circle.__init__(self,x,y,r)
        self.h=h
        Cylinder.cylinders_count+=1

    def print(self):
        Circle.print(self)
        print("h=",self.h)

    def base_area(self):
        return Circle.area(self)

    def area(self):
        return 2*self.base_area()+Circle.circumference(self)*self.h

    def volume(self):
        return self.base_area()*self.h

    def print_total():
        print('Total Cylinders:',Cylinder.cylinders_count)


p=Point(3,4)
p.print()
print(p.distance())
print(p.distance(1,1))
p.translate(2,2)
print(p.distance())

print('\n--------------------\n')

c=Circle(2,2,5)
c.print()
print(c.distance(1,0))
print(c.circumference())
print(c.area())

print('\n--------------------\n')

cy=Cylinder(0,0,10,100)
cy.print()
print(cy.distance())
print(cy.circumference())
print(cy.base_area())
print(cy.area())
print(cy.volume())

print('\n--------------------\n')

Point.print_total()
Circle.print_total()
Cylinder.print_total()


