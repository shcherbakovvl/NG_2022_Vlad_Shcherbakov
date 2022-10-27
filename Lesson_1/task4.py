# importing library math for sqrt function
import math

# function that calculating discriminant and roots
def formula():
    d = (b * b) - (4 * a * c)
    print ("======================================")
    print ("Discriminant = ", d)
    print ("======================================")
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("There is two roots. First(x1) = %.2f, second(x2) = %.2f" % (x1, x2))
    elif d == 0:
        x = (-b + math.sqrt(d)) / 2 * a
        print("There is only one root and it equals ",x)
    else:
        print("There is no roots")

print ("======================================")
print ("You using a calculator of Quadratic Formula(ax^2 + bx + c = 0)")
print ("======================================")
a = int(input("Enter number for a: "))
b = int(input("Enter number for b: "))
c = int(input("Enter number for c: "))
formula()
print ("======================================")