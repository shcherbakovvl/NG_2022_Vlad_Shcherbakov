# these functions do math calculations
def addition(firstNumber, secondNumber):
    result = firstNumber + secondNumber
    print ("Sum of", firstNumber, "and", secondNumber, "is", result)
def substraction(firstNumber, secondNumber):
    result = firstNumber - secondNumber
    print ("Difference between", firstNumber, "and", secondNumber, "is", result)
def multiplication(firstNumber, secondNumber):
    result = firstNumber * secondNumber
    print ("Product of", firstNumber, "and", secondNumber, "is", result)
def division(firstNumber, secondNumber):
    result = firstNumber / secondNumber
    print ("Quotient of", firstNumber, "and", secondNumber, "is", result)

print ("======================================")
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
result = int
print ("======================================")
func = str(input("Choose ariphmetic operation(+, -, *, /): "))
print ("======================================")

# functions call
if "+" in func:
    addition(firstNumber, secondNumber)
elif "-" in func:
    substraction(firstNumber, secondNumber)
elif "*" in func:
    multiplication(firstNumber, secondNumber)
elif "/" in func:
    division(firstNumber, secondNumber)

print ("======================================")