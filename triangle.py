# FizzBuzz Unit 6 assignment 6.13 - Triangle class
# Create a Triangle class from 3 triangle sides and add a few methods to it

from math import sqrt

class Triangle():
    # constructor: a, b, and c are the side lenghts
    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3
    
    # perimeter: calculate the perimeter of the triangle
    def perimeter(self):
        return self.a + self.b + self.c

    # area: calculate the area of the triangle
    def area(self):
        semi_perimeter = self.perimeter() / 2
        triangle_area = sqrt(semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter - self.c))
        return triangle_area

    # scale: create a new Triangle scaling up the sides by a scale factor
    def scale(self, scale_factor):
        return Triangle(self.a * scale_factor, self.b * scale_factor, self.c * scale_factor)

    # check if the triangle is valid (possible to create) with the given sides
    # if the sum of two sides is greater than the length of the third for each side of the triangle, then it's a valid one 
    def is_valid(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        return False

    # check if the triangle is a 'right' one (with one angle at 90 degrees)
    # if the sum of squares of two minor sides is equal to the square of the longer side, then it is a right triangle
    def is_right(self):
        if (self.a*self.a + self.b*self.b == self.c*self.c) or (self.a*self.a + self.c*self.c == self.b*self.b) or (self.b*self.b + self.c*self.c == self.a*self.a):
            return True
        return False 

# Output
print()
print("Let's create a triangle!")
print()

# initialize the Triangle
t = Triangle(4, 4, 7)

print("It has the following sides: %d, %d, and %d." % (t.a, t.b, t.c))

# Case 1: show additional info if the triangle is valid (possible to draw)
if t.is_valid():
    print("With these sides it is a valid triangle.")
    print()
    print("The perimeter of this triangle is %d." % t.perimeter())
    print("The area of the triangle is %d." % t.area())
    if t.is_right():
        print("And this is also a right triangle!")
    else:
        print("This triangle is not a right triangle.")
    print()

    # create another, scaled triangle
    scale = 3
    print("We now create a new triangle by scaling the one we have by %s." % scale)
    
    r = t.scale(scale)

    print("The new triangle has the following sides: %d, %d, and %d." % (r.a, r.b, r.c))
    print("It is still a valid triangle!")
    print("The perimeter of the new triangle is %d." % r.perimeter())
    print("The area of the new triangle is %d." % r.area())
    if r.is_right():
        print("And this is a right trianlge!")
    else:
        print("This is not a right triangle.")

# Case 2: report if the triangle not valid
else:
    print("The triangle is not possible to construct with the given sides.")

print()