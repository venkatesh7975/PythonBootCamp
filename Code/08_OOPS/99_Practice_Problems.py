# ==========================================
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
