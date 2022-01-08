""""
Author: Atahan Koc
Description Part: This progrram will ask the user to enter the coefficients for a system of two homogeneous equations, a, b, c, and d.
The program will next determine whether the equation is solvable and, if so, print the solution. 'The equation has no solution' will be printed if this is not the case.
"""

class HomogenEquation:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
   # If ad - bc is not 0, the method isSolvable() returns True.
    def isSolvable(self):
        return self.a * self.d - self.b * self.c != 0

    def getXY(self):
       # The equations are independent in this case. so, the system only has one solution.
        return (0, 0)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

equation = HomogenEquation(a, b, c, d)

# if the equation is not solvable, print 'The equation has no solution'
if not equation.isSolvable():
    print("\nThe equation has no solution")
else:
    x, y = equation.getXY()
    print("\nThe solution is: (" + str(x) + ", " + str(y) + ")")