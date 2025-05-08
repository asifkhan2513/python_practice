## identifier 
# Variable is a name that refers to a value.
# A variable is created the moment you first assign a value to it.  
x = 5  # X is Identifier
y = 10 

#Keywords in python
# Keywords are reserved words in Python that have special meaning to the interpreter.
# Keywords cannot be used as identifiers (variable names).
# Keywords are case-sensitive.

#if =5  if is a keyword in python so it will give an error
 # Identation
# Indentation refers to the spaces at the beginning of a code line.
# Python uses indentation to indicate a block of code.

a =10
if(a <6):
    print("a is less than 6")
else:
    print("a is greater than 6")
    
    
# Getting input from user
##name  = input("Enter your name: ")  # by using input function we can get input from user
#print("Hello", name)


# data types in python
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range
# 3. Set Types: set, frozenset
# 4. Mapping Type: dictionary
# 5. Boolean Type: bool
# 6. Binary Types: bytes, bytearray, memoryview
# 7. None Type: NoneType

n1  = 10 
n2  = 20.5
n3 = 1j
print(type(n1))  # <class 'int'>
print(type(n2))  # <class 'float'>
print(type(n3))  # <class 'complex'>

l1 = ["apple", "banana", "cherry"] # list is a collection of items in a particular order.
l2 = ("apple", "banana", "cherry") # tuple is a collection of items that is ordered and unchangeable.
l3 = range(6)
print(type(l1))  # <class 'list'>   
print(type(l2))  # <class 'tuple'>
print(type(l3))  # <class 'range'>


 #function 
# A function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
  print("my name is ASIF KHAN")  # Function definition

my_function()  # Call the function
my_function()  # Call the function again
my_function()  # Call the function again
my_function()  # Call the function again

#  try your self to create a function that takes two numbers as arguments and returns their sum.

def sum (a, b):
    return a + b

print(sum(10, 20))
print(sum(40, 30))
print(sum(60, 40))



# Method
# A method is a function that belongs to an object.
# In Python, methods are functions that are associated with an object.
# Methods are called on objects, and they can access and modify the object's data.
# Methods are defined within a class and are used to perform operations on the objects of that class.   

import math  # math is a module that provides mathematical functions and constants
print(math.pi)

m = 18.9
print(math.ceil(m))
print(math.sqrt(64))

m1 = -10
print(abs(m1))  # abs() returns the absolute value of a number.
print(math.fabs(m1))  # fabs() returns the absolute value of a number as a float.
print(math.factorial(5))  # factorial() returns the factorial of a number.
print(math.pow(2, 3))  # pow() returns the value of x to the power of y.