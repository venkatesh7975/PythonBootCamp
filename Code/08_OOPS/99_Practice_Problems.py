# Interactive Practice Problems - Module 8 (OOPS)
import time

def quiz():
    print("Welcome to the Module 8 Practice Quiz! (OOPS)")
    print("Press Enter to reveal the answer to each question.")
    print("-" * 50)
    
    questions = [
        ("Define a class `Cat` with an empty body.", 
         "class Cat: pass"),
         
        ("Create an instance of `Cat` named `whiskers`.", 
         "whiskers = Cat()"),
         
        ("Add an `__init__` method to `Cat` that sets `name`.", 
         "def __init__(self, name): self.name = name"),
         
        ("Add a `meow` method that prints 'Meow! I am [name]'.", 
         "def meow(self): print(f'Meow! I am {self.name}')"),
         
        ("Create a class `Car` with `model` and `year`.", 
         "class Car: def __init__(self, m, y)..."),
         
        ("Create two cars. Change the year of one of them.", 
         "c1.year = 2025"),
         
        ("Add a class variable `wheels = 4` to `Car`. Print it for both cars.", 
         "class Car: wheels=4"),
         
        ("Create a class `Student` with `_grade` (private).", 
         "self._grade = 0"),
         
        ("Add a getter and setter for `grade` preventing negative values.", 
         "@property def grade..."),
         
        ("Create `class Animal` and `class Dog(Animal)`. Show inheritance.", 
         "class Dog(Animal): ..."),
         
        ("Use `super()` in `Dog.__init__`.", 
         "super().__init__()"),
         
        ("Create a static method `Math.add(a, b)`.", 
         "@staticmethod def add(a,b)..."),
         
        ("Create a class method `Person.create_anonymous()`.", 
         "@classmethod def create(cls)..."),
         
        ("Override `__str__` for `Cat` to return 'Cat: [name]'.", 
         "def __str__(self): return f'Cat: {self.name}'"),
         
        ("Create a `dataclass` called `InventoryItem`.", 
         "@dataclass class InventoryItem: name: str"),
         
        ("Use `__slots__` to limit attributes to `name` and `age`.", 
         "__slots__ = ['name', 'age']"),
         
        ("Create two classes `A` and `B` with same method `hi()`. Iterate and call (Polymorphism).", 
         "[A(), B()] loop"),
         
        ("Create an Abstract Base Class `Shape` with abstract method `draw`.", 
         "class Shape(ABC): @abstractmethod def draw(self): pass"),
         
        ("Implement `overloading` for `__add__` (Vector addition).", 
         "def __add__(self, other): return Vector(self.x+other.x...)"),
         
        ("Demonstrate Composition: A `Computer` has a `CPU` object.", 
         "class Computer: def __init__(self): self.cpu = CPU()")
    ]
    
    for i, (q, a) in enumerate(questions, 1):
        print(f"\\nQ{i}: {q}")
        input("   Your Answer: ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
