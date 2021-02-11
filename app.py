from addition import add
from  subtraction import subtract
from multiplication import multiply
from division import divide


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y 

def divide(x,y):
    return x / y

#take input from user
print ("Welcome to simple calculator, please select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("Enter choice 1/2/3/4:")


num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter the second number:"))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))
elif choice == '3':
    print(num1, "x", num2, "=", multiply(num1,num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("Invalid input")




