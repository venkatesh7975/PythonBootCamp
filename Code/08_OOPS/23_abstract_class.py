# 23. Abstract Class
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
