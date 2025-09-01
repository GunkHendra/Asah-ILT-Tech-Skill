print('Hello, World!')

# Data Types in Python
str2 = "Hello, World!"
int = 20
float = 20.5
complex = 1j
my_range = range(6)
bool = True
frozenset = frozenset({"apple", "banana", "cherry"})
bytes = b"Hello"
bytearray = bytearray(5)
NoneType = None

# Operator
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division
print(a > b)  # Greater than
print(a < b)  # Less than
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
print(a and b)  # Logical AND
print(a or b)  # Logical OR
print(not a)  # Logical NOT
print(a is b)  # Identity
print(a is not b)  # Not Identity
list = [1, 2, 3, 4, 5]
print(a in list)  # Membership
print(a not in list)  # Not Membership

# Control Flow
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

match a:
    case 10:
        print("a is 10")
    case 20:
        print("a is 20")
    case _:
        print("a is neither 10 nor 20")

for i in range(5): # Used when the number of iterations is known
    print(i)
    if i == 3:
        break # Exit the loop when i is 3

while a > b: # Used when the number of iterations is unknown for more dynamic looping
    print(a)
    a -= 1
    if a == b:
        continue # Skip the rest of the loop when a equals b

# Data Structures
list = ["apple", "banana", "cherry"] # Ordered, mutable, allows duplicates
print(list) # Note: Lists are defined by square brackets
tuple = ("apple", "banana", "cherry") # Ordered, immutable, allows duplicates
print(tuple) # Note: Tuples are defined by parentheses, but can also be defined without them
# Tuple without parentheses
tuple2 = "apple", "banana", "cherry"
print(tuple2) # Note: Both tuple and tuple2 are tuples
set = {"apple", "banana", "cherry"} # Unordered, mutable, no duplicates
print(set) # Note: The order of elements in a set may vary each time you run the code
dict = {"name": "John", "age": 36} # Ordered (as of Python 3.7), mutable, no duplicate keys
print(dict) # Note: Dictionaries are defined by curly braces
str2 = "Hello, World!" # Ordered, immutable, allows duplicates, how is string ordered? By index position of each character
print(str2) # Note: Strings are defined by either single or double quotes
str3 = '''Hello,
World!''' # Multi-line string
print(str3) # Note: Multi-line strings are defined by triple quotes

# Functions & Procedures
def my_function(name):
    return ("Hello, " + name)

def my_procedure():
    print("Hello, World!")

print(my_function("Alice"))
my_procedure()

# Element Manipulation
list.append("orange") # Add an element to the end of the list
print(list)
list.remove("banana") # Remove an element from the list
print(list)
list.pop(1) # Remove an element at a specific index
print(list)
list.insert(1, "kiwi") # Add an element at a specific index
print(list)
list.sort() # Sort the list
print(list)
list.reverse() # Reverse the list
print(list)
list.clear() # Remove all elements from the list
print(list)
list = ["apple", "banana", "cherry"]
del list[0] # Delete the first element of the list
del list # Delete the list
# Delete and pop are similar, but pop returns the removed element, while del does not
list = ["apple", "banana", "cherry"]
print(list.pop(1)) # This will print "banana"

# Slicing
print(str2[0:5:2]) # Start at index 0, end at index 5, step by 2

# OOP
class MyClass:
    # Attributes
    name = ""
    age = 0
    student = True

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method
    def my_method(self):
        return ("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

obj = MyClass("Alice", 30)
print(obj.my_method())

# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Method
class AnotherClass:
    # Object Method
    def my_method(self):
        print("This is an object method.")
    # Static Method
    @staticmethod
    def my_staticmethod():
        print("This is a static method.")
    # Class Method
    @classmethod
    def my_classmethod(cls):
        print("This is a class method.")
obj2 = AnotherClass()
obj2.my_method()
AnotherClass.my_staticmethod()
AnotherClass.my_classmethod()

# Inheritance
class ParentClass:
    def my_method(self):
        print("This is a method from the parent class.")

class ChildClass(ParentClass):
    def my_method(self):
        print("This is a method from the child class.")
        super().my_method()

obj3 = ChildClass()
obj3.my_method()
# Note: The child class method overrides the parent class method, but can still call it using super()

# Override
class BaseClass:
    def my_method(self):
        print("This is a method from the base class.")
class SubClass(BaseClass):
    def my_method(self):
        print("This is a method from the subclass.")
obj4 = SubClass()
obj4.my_method()
# Note: The subclass method overrides the base class method

# Super
class SuperClass:
    def my_method(self):
        print("This is a method from the superclass.")
class SubClass2(SuperClass):
    def my_method(self):
        super().my_method()
        print("This is a method from the subclass.")
obj5 = SubClass2()
obj5.my_method()
# Note: The subclass method overrides the superclass method, but can still call it using super()

# Unit Testing
import unittest

# Simple functions to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Unit test class
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()