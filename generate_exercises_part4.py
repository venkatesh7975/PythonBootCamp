import os

# Base Directory
BASE_DIR = "Code"

# Helper Function to Create Files
def create_file(module, filename, content):
    path = os.path.join(BASE_DIR, module)
    os.makedirs(path, exist_ok=True)
    
    full_path = os.path.join(path, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {full_path}")

# ==========================================
# MODULE 7: Functions
# ==========================================
m7 = "07_Functions"

create_file(m7, "01_define.py", """# 1. Define Function
# ==========================================
# CONCEPT: Reuse
# ==========================================
# Define once, use many times.

def say_hello():
    print("Hello from a function!")

# Nothing happens until we call it!
""")

create_file(m7, "02_call.py", """# 2. Call Function
# ==========================================
# CONCEPT: Execution
# ==========================================
# Use parentheses () to run the function.

def say_hello():
    print("Hello!")

say_hello()
say_hello() 
# Prints Hello twice.
""")

create_file(m7, "03_params.py", """# 3. Parameters
# ==========================================
# CONCEPT: Input
# ==========================================
# Pass data INTO the function using arguments.

def greet(name):
    print(f"Hello, {name}")

greet("Alice")
greet("Bob")
""")

create_file(m7, "04_return.py", """# 4. Return Value
# ==========================================
# CONCEPT: Output
# ==========================================
# Send data OUT of the function.

def add(a, b):
    return a + b

result = add(5, 3)
print(result) # 8
""")

create_file(m7, "05_none_return.py", """# 5. Implicit Return (None)
# ==========================================
# CONCEPT: Void
# ==========================================
# If no return statement, Python returns None.

def no_return():
    print("I return nothing.")

val = no_return()
print(val) # None
""")

create_file(m7, "06_default_args.py", """# 6. Default Arguments
# ==========================================
# CONCEPT: Fallback
# ==========================================
# Optional parameters.

def greet(name="User"):
    print(f"Hello, {name}")

greet("Alice") # Hello, Alice
greet()        # Hello, User
""")

create_file(m7, "07_keyword_args.py", """# 7. Keyword Arguments
# ==========================================
# CONCEPT: Named Input
# ==========================================
# Order doesn't matter if you use names.

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

# Correct
describe_pet(animal="Dog", name="Rex")
# Also Correct (Order swapped!)
describe_pet(name="Rex", animal="Dog")
""")

create_file(m7, "08_arbitrary_args.py", """# 8. Arbitrary Args (*args)
# ==========================================
# CONCEPT: Unlimited Input
# ==========================================
# Collects extra arguments into a Tuple.

def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all(1, 2, 3, 4)) # 10
""")

create_file(m7, "09_kwargs.py", """# 9. Arbitrary Keywords (**kwargs)
# ==========================================
# CONCEPT: Dictionary Input
# ==========================================
# Collects named arguments into a Dictionary.

def build_profile(**user_info):
    print(user_info)

build_profile(name="Alice", age=30, job="Dev")
# {'name': 'Alice', 'age': 30, 'job': 'Dev'}
""")

create_file(m7, "10_scope_local.py", """# 10. Local Scope
# ==========================================
# CONCEPT: Privacy
# ==========================================
# Variables inside a function are invisible outside.

def my_func():
    secret = "I am hidden"

# print(secret) # NameError: name 'secret' is not defined
""")

create_file(m7, "11_scope_global.py", """# 11. Global Scope
# ==========================================
# CONCEPT: Visibility
# ==========================================
# Variables defined outside are visible inside.

x = "Global"

def show_x():
    print(x) # Works!

show_x()
""")

create_file(m7, "12_global_keyword.py", """# 12. Global Keyword
# ==========================================
# CONCEPT: Modification
# ==========================================
# To CHANGE a global variable, declare it global inside function.

count = 0

def increment():
    global count
    count += 1

increment()
print(count) # 1
""")

create_file(m7, "13_recursion.py", """# 13. Recursion
# ==========================================
# CONCEPT: Self-Calling
# ==========================================
# A function calling itself. Must have a Stop Condition (Base Case).

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120
""")

create_file(m7, "14_recursion_limit.py", """# 14. Recursion Limit
# ==========================================
# CONCEPT: Safety Net
# ==========================================
# Python stops infinite recursion to save memory. 
# Usually 1000 calls deep.

import sys
print(sys.getrecursionlimit())

def infinite():
    infinite()

# infinite() # RecursionError
""")

create_file(m7, "15_lambda.py", """# 15. Lambda Functions
# ==========================================
# CONCEPT: Anonymous Function
# ==========================================
# One-liner function. lambda inputs : output

# Normal
def add(x, y):
    return x + y

# Lambda
add_lambda = lambda x, y : x + y

print(add_lambda(5, 3)) # 8
""")

create_file(m7, "16_map_lambda.py", """# 16. Map with Lambda
# ==========================================
# CONCEPT: Transformation
# ==========================================
# Apply function to every item in list.

nums = [1, 2, 3]
doubled = list(map(lambda x: x*2, nums))
print(doubled) # [2, 4, 6]
""")

create_file(m7, "17_filter_lambda.py", """# 17. Filter with Lambda
# ==========================================
# CONCEPT: Selection
# ==========================================
# Keep only items where function returns True.

nums = [1, -1, 2, -5]
positives = list(filter(lambda x: x > 0, nums))
print(positives) #[1, 2]
""")

create_file(m7, "18_docstring.py", """# 18. Docstrings
# ==========================================
# CONCEPT: Documentation
# ==========================================
# Triple quotes describing what the function does.
# Stored in .__doc__

def square(n):
    '''Takes a number n and returns n squared.'''
    return n**2

print(square.__doc__)
""")

create_file(m7, "19_type_hints.py", """# 19. Type Hints
# ==========================================
# CONCEPT: Clarity
# ==========================================
# Optional hints about types. Python ignores them but IDEs love them.

def greet(name: str) -> str:
    return "Hello " + name

# greet(123) # IDE might warn you, but Python runs it.
""")

create_file(m7, "20_inner_func.py", """# 20. Inner Functions
# ==========================================
# CONCEPT: Encapsulation
# ==========================================
# Helper functions hidden inside.

def outer():
    print("Outer")
    
    def inner():
        print("Inner")
    
    inner()

outer()
# inner() # Error, not visible here.
""")

create_file(m7, "21_closure.py", """# 21. Closure
# ==========================================
# CONCEPT: Function Factory
# ==========================================
# Inner function remembers outer variables even after outer finishes.

def multiplier(n):
    # Returns a function that multiplies by n
    return lambda x: x * n

times3 = multiplier(3)
times5 = multiplier(5)

print(times3(10)) # 30
print(times5(10)) # 50
""")

create_file(m7, "22_decorator_simple.py", """# 22. Decorator Wrapper
# ==========================================
# CONCEPT: Wrapping
# ==========================================
# Adds behavior before/after a function without changing it.

def my_decorator(func):
    def wrapper():
        print("Before function.")
        func()
        print("After function.")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()
""")

create_file(m7, "23_generator.py", """# 23. Generator
# ==========================================
# CONCEPT: Lazy Evaluation
# ==========================================
# Uses yield instead of return. Returns an iterator.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(3)
print(next(counter)) # 1
print(next(counter)) # 2
""")

create_file(m7, "24_yield.py", """# 24. Yield Expression
# ==========================================
# CONCEPT: Saving State
# ==========================================
# Generator expression (like list comp but lazy).

g = (x*x for x in range(3))
print(list(g)) # [0, 1, 4]
""")

create_file(m7, "25_try_except.py", """# 25. Try Except
# ==========================================
# CONCEPT: Error Handling
# ==========================================
# Catch specific errors.

try:
    print(10/0)
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(f"Other error: {e}")
""")

create_file(m7, "26_finally.py", """# 26. Finally Block
# ==========================================
# CONCEPT: Cleanup
# ==========================================
# Runs no matter what.

try:
    f = open("data.txt", "w")
    f.write("Hi")
except:
    print("Error")
finally:
    f.close() # Always close file!
    print("Closed file.")
""")

create_file(m7, "27_raise.py", """# 27. Raise Exception
# ==========================================
# CONCEPT: Trigger Error
# ==========================================
# Manually cause an error.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")

# check_age(-5) # Crashes with ValueError
""")

create_file(m7, "28_assert.py", """# 28. Assert
# ==========================================
# CONCEPT: Sanity Check
# ==========================================
# Used for debugging. If false, crashes with AssertionError.

x = 10
assert x > 0, "x should be positive"
# assert x < 0, "x should be negative" # Crash
""")

create_file(m7, "29_custom_error.py", """# 29. Custom Exception
# ==========================================
# CONCEPT: Specificity
# ==========================================
# Create your own error type.

class TooColdError(Exception):
    pass

temp = -10
if temp < 0:
    # raise TooColdError("Brrr!")
    pass
""")

create_file(m7, "30_stack_trace.py", """# 30. Stack Trace (Traceback)
# ==========================================
# CONCEPT: Debugging Trail
# ==========================================
# Python prints the path to the error.

import traceback

try:
    print(1/0)
except:
    traceback.print_exc() # Prints the error details
""")

create_file(m7, "99_Practice_Problems.py", """# ==========================================
# MODULE 7: PRACTICE PROBLEMS
# ==========================================
# 1. Define a function `greet(name)` that prints "Hello, [name]".
# 2. Define `add(a, b)` that returns sum. Call it with 5, 10.
# 3. Write a function with a default argument `country="Unknown"`.
# 4. Write a function that accepts `*args` and prints the count of arguments.
# 5. Write a function that accepts `**kwargs` and prints all keys.
# 6. Create a global variable `count` and increment it inside a function.
# 7. Write a recursive function to calculate factorial of n.
# 8. Use `map` and `lambda` to square a list of numbers.
# 9. Use `filter` and `lambda` to get even numbers from a list.
# 10. Write a function with a Docstring and print the docstring.
# 11. Create a simple generator that yields "A", "B", "C".
# 12. Write a function nested inside another function.
# 13. Create a decorator that prints "Running..." before the function.
# 14. Handle a `ValueError` when converting user input string to int.
# 15. Use `finally` to print "Done" after a try-except block.
# 16. Raise a `TypeError` if an argument `n` is not an int.
# 17. Use assert to check if `2+2 == 4`.
# 18. Write a function that returns MULTIPLE values (e.g. min and max) (Return tuple).
# 19. Create a lambda that adds 10 to a number.
# 20. Write a recursive function to print a countdown.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. def greet(n):...
2. def add(a,b): return a+b
3. def origin(country="Unknown"):...
4. def count_args(*args): print(len(args))
5. def print_keys(**kwargs): print(kwargs.keys())
6. global count; count+=1
7. if n==1: return 1 else n*fact(n-1)
8. list(map(lambda x: x**2, L))
9. list(filter(lambda x: x%2==0, L))
10. def f(): "Doc"; ...; print(f.__doc__)
11. def gen(): yield "A"...
12. def out(): def in():...
13. def dec(f): def wrap(): print("Run"); f(); return wrap
14. try: int("a") except ValueError: ...
15. finally: print("Done")
16. if not isinstance(n, int): raise TypeError
17. assert 2+2==4
18. return min(L), max(L)
19. f = lambda x: x+10
20. def cd(n): if n>0: print(n); cd(n-1)
'''
""")


# ==========================================
# MODULE 8: OOPS
# ==========================================
m8 = "08_OOPS"

create_file(m8, "01_class_def.py", """# 1. Class Definition
# ==========================================
# CONCEPT: Blueprint
# ==========================================
# A class defines a new data type.

class Dog:
    pass # Empty class

print(Dog)
""")

create_file(m8, "02_object_creation.py", """# 2. Object Creation
# ==========================================
# CONCEPT: Instantiation
# ==========================================
# Making a specific object from the blueprint.

class Dog:
    pass

d = Dog() # Create instance
print(d)
""")

create_file(m8, "03_init.py", """# 3. Constructor (__init__)
# ==========================================
# CONCEPT: Setup
# ==========================================
# Runs automatically when object is created.

class Dog:
    def __init__(self):
        print("A new dog is born!")

d = Dog() # Prints message immediately
""")

create_file(m8, "04_self.py", """# 4. Self
# ==========================================
# CONCEPT: Identity
# ==========================================
# 'self' refers to the specific object being used.
# It allows each object to have its own data.

class Dog:
    def __init__(self, name):
        self.name = name # My name is [name]

d1 = Dog("Rex")
d2 = Dog("Spot")
print(d1.name)
print(d2.name)
""")

create_file(m8, "05_attributes.py", """# 5. Attributes (Variables)
# ==========================================
# CONCEPT: Data
# ==========================================
# Variables stored inside an object.

class Car:
    pass

c = Car()
c.color = "Red" # Dynamic attribute
print(c.color)
""")

create_file(m8, "06_methods.py", """# 6. Methods (Functions)
# ==========================================
# CONCEPT: Action
# ==========================================
# Functions inside a class. Must have 'self' as first arg.

class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()
""")

create_file(m8, "07_class_var.py", """# 7. Class Variables
# ==========================================
# CONCEPT: Shared Data
# ==========================================
# Shared by ALL objects of that class.

class Dog:
    kind = "Canine" # Class Variable

d1 = Dog()
d2 = Dog()
print(d1.kind) # Canine
print(d2.kind) # Canine
""")

create_file(m8, "08_instance_var.py", """# 8. Instance Variables
# ==========================================
# CONCEPT: Unique Data
# ==========================================
# Unique to EACH object. Defined in __init__ using self.

class Dog:
    def __init__(self, name):
        self.name = name

d1 = Dog("A")
d2 = Dog("B")
# d1.name is A, d2.name is B
""")

create_file(m8, "09_inheritance.py", """# 9. Inheritance
# ==========================================
# CONCEPT: Hierarchy
# ==========================================
# Child class gets everything from Parent class.

class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal): # Dog inherits from Animal
    def bark(self):
        print("Woof")

d = Dog()
d.eat() # Inherited!
d.bark()
""")

create_file(m8, "10_super.py", """# 10. Super()
# ==========================================
# CONCEPT: Parent Access
# ==========================================
# Calls the parent method. Useful in __init__.

class Animal:
    def __init__(self):
        print("Animal Created")

class Dog(Animal):
    def __init__(self):
        super().__init__() # Call parent init
        print("Dog Created")

d = Dog()
""")

create_file(m8, "11_polymorphism.py", """# 11. Polymorphism
# ==========================================
# CONCEPT: Many Forms
# ==========================================
# Different classes having same method name.

class Cat:
    def speak(self): print("Meow")

class Dog:
    def speak(self): print("Woof")

animals = [Cat(), Dog()]
for a in animals:
    a.speak() # Knows which one to call!
""")

create_file(m8, "12_encapsulation.py", """# 12. Encapsulation (Private)
# ==========================================
# CONCEPT: Hiding
# ==========================================
# _name (Weak private, convention)
# __name (Strong private, mangled)

class Account:
    def __init__(self):
        self._balance = 0 # Private-ish

a = Account()
# We should access it via methods, but python allows direct access if we really want.
""")

create_file(m8, "13_mangling.py", """# 13. Name Mangling
# ==========================================
# CONCEPT: Strong Hiding
# ==========================================

class Secret:
    def __init__(self):
        self.__code = 1234

s = Secret()
# print(s.__code) # Error!
print(s._Secret__code) # The back door way to access it.
""")

create_file(m8, "14_getter_setter.py", """# 14. Getters and Setters
# ==========================================
# CONCEPT: Controlled Access
# ==========================================
# Use @property to make methods look like variables.

class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age can't be negative")
        else:
            self._age = value

p = Person(10)
p.age = -5 # Validation runs!
""")

create_file(m8, "15_static_method.py", """# 15. Static Method
# ==========================================
# CONCEPT: Utility
# ==========================================
# Belongs to class but doesn't need self.

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 5))
""")

create_file(m8, "16_class_method.py", """# 16. Class Method
# ==========================================
# CONCEPT: Factory
# ==========================================
# Takes 'cls' instead of 'self'. Can create objects.

class Person:
    kind = "Human"
    
    @classmethod
    def get_kind(cls):
        return cls.kind

print(Person.get_kind())
""")

create_file(m8, "17_magic_str.py", """# 17. Magic Method (__str__)
# ==========================================
# CONCEPT: String Representation
# ==========================================
# Controls what print(obj) shows.

class Dog:
    def __str__(self):
        return "I am a Dog"

d = Dog()
print(d)
""")

create_file(m8, "18_magic_repr.py", """# 18. Magic Method (__repr__)
# ==========================================
# CONCEPT: Developer String
# ==========================================
# Output for developers/debugging.

class Dog:
    def __repr__(self):
        return "Dog()"

d = Dog()
print(repr(d))
""")

create_file(m8, "19_magic_add.py", """# 19. Operator Overloading (+)
# ==========================================
# CONCEPT: Custom Math
# ==========================================
# Define what + does for your objects.

class Point:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, other):
        return Point(self.x + other.x)

p1 = Point(10)
p2 = Point(20)
p3 = p1 + p2
print(p3.x) # 30
""")

create_file(m8, "20_magic_len.py", """# 20. Magic Method (__len__)
# ==========================================
# CONCEPT: Size
# ==========================================
# Controls len(obj).

class Cart:
    items = ["A", "B", "C"]
    
    def __len__(self):
        return len(self.items)

c = Cart()
print(len(c)) # 3
""")

create_file(m8, "21_mult_inheritance.py", """# 21. Multiple Inheritance
# ==========================================
# CONCEPT: Mixing Parents
# ==========================================
# Inheriting from two classes.

class A:
    def method_a(self): print("A")

class B:
    def method_b(self): print("B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()
""")

create_file(m8, "22_mro.py", """# 22. MRO (Method Resolution Order)
# ==========================================
# CONCEPT: Search Order
# ==========================================
# Where does python look for methods first?

class A: pass
class B(A): pass
class C(B): pass

print(C.mro()) # C -> B -> A -> Object
""")

create_file(m8, "23_abstract_class.py", """# 23. Abstract Class
# ==========================================
# CONCEPT: Enforcing Rules
# ==========================================
# Use ABC (Abstract Base Class). Children MUST implement methods.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14

# s = Shape() # Error! Can't instantiate abstract class.
c = Circle()
""")

create_file(m8, "24_isinstance.py", """# 24. isinstance()
# ==========================================
# CONCEPT: Type Checking
# ==========================================
# Check if object belongs to a class.

d = Dog() # From earlier
print(isinstance(d, Dog)) # True
""")

create_file(m8, "25_issubclass.py", """# 25. issubclass()
# ==========================================
# CONCEPT: Relation Check
# ==========================================
# Check if class is child of another.

class A: pass
class B(A): pass

print(issubclass(B, A)) # True
""")

create_file(m8, "26_slots.py", """# 26. __slots__
# ==========================================
# CONCEPT: Optimization
# ==========================================
# Prevents creating dynamic attributes to save memory.

class Point:
    __slots__ = ['x', 'y']

p = Point()
p.x = 10
# p.z = 5 # Error! Not in slots.
""")

create_file(m8, "27_dataclass.py", """# 27. Dataclasses
# ==========================================
# CONCEPT: Data Holder
# ==========================================
# Python writes __init__ and __repr__ for you!

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(10, 20)
print(p) # Point(x=10, y=20)
""")

create_file(m8, "28_enums.py", """# 28. Enums
# ==========================================
# CONCEPT: Constants
# ==========================================
# Enumerations for fixed options.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.RED)
""")

create_file(m8, "29_composition.py", """# 29. Composition
# ==========================================
# CONCEPT: Has-A Relation
# ==========================================
# An object CONTAINING other objects (Use variables instead of inheritance).

class Engine:
    def start(self): print("Vroom")

class Car:
    def __init__(self):
        self.engine = Engine() # Car HAS AN Engine
    
    def drive(self):
        self.engine.start()

c = Car()
c.drive()
""")

create_file(m8, "30_destructor.py", """# 30. Destructor (__del__)
# ==========================================
# CONCEPT: Cleanup
# ==========================================
# Runs when object is deleted. (Rarely used, but good to know).

class FileHandler:
    def __del__(self):
        print("File Closed.")

f = FileHandler()
del f # Triggers __del__
""")

create_file(m8, "99_Practice_Problems.py", """# ==========================================
# MODULE 8: PRACTICE PROBLEMS
# ==========================================
# 1. Define a class `Cat` with an empty body.
# 2. Create an instance of `Cat` named `whiskers`.
# 3. Add an `__init__` method to `Cat` that sets `name`.
# 4. Add a `meow` method that prints "Meow! I am [name]".
# 5. Create a class `Car` with `model` and `year`.
# 6. Create two cars. Change the year of one of them.
# 7. Add a class variable `wheels = 4` to `Car`. Print it for both cars.
# 8. Create a class `Student` with `_grade` (private).
# 9. Add a getter and setter for `grade` preventing negative values.
# 10. Create `class Animal` and `class Dog(Animal)`. Show inheritance.
# 11. Use `super()` in `Dog.__init__`.
# 12. Create a static method `Math.add(a, b)`.
# 13. Create a class method `Person.create_anonymous()`.
# 14. Override `__str__` for `Cat` to return "Cat: [name]".
# 15. Create a `dataclass` called `InventoryItem`.
# 16. Use `__slots__` to limit attributes to `name` and `age`.
# 17. Create two classes `A` and `B` with same method `hi()`. Iterate and call (Polymorphism).
# 18. Create an Abstract Base Class `Shape` with abstract method `draw`.
# 19. Implement `overloading` for `__add__` (Vector addition).
# 20. Demonstrate Composition: A `Computer` has a `CPU` object.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. class Cat: pass
2. whiskers = Cat()
3. def __init__(self, name): self.name = name
4. def meow(self): print(f"Meow! I am {self.name}")
5. class Car: def __init__(self, m, y)...
6. c1.year = 2025
7. class Car: wheels=4
8. self._grade = 0
9. @property def grade...
10. class Dog(Animal): ...
11. super().__init__()
12. @staticmethod def add(a,b)...
13. @classmethod def create(cls)...
14. def __str__(self): return f"Cat: {self.name}"
15. @dataclass class InventoryItem: name: str
16. __slots__ = ['name', 'age']
17. [A(), B()] loop
18. class Shape(ABC): @abstractmethod def draw(self): pass
19. def __add__(self, other): return Vector(self.x+other.x...)
20. class Computer: def __init__(self): self.cpu = CPU()
'''
""")

print("Generated Modules 7 & 8!")
