# these functions do math calculations
def addition(a, b):
    result = a + b
    print ("Sum of", a, "and", b, "is", result)
def substraction(a, b):
    result = a - b
    print ("Difference between ", a, "and", b, "is", result)
def multiplication(a, b):
    result = a * b
    print ("Product of", a, "and", b, "is", result)
def division(a, b):
    result = a / b
    print ("Quotient of", a, "and", b, "is", result)

print ("======================================")
a = int(input("Enter first number(a): "))
b = int(input("Enter second number(b): "))
result = int
print ("======================================")
func = str(input("Choose ariphmetic operation(+, -, *, /): "))
print ("======================================")

# functions call
if "+" in func:
    addition(a, b)
elif "-" in func:
    substraction(a, b)
elif "*" in func:
    multiplication(a, b)
elif "/" in func:
    division(a, b)

print ("======================================")