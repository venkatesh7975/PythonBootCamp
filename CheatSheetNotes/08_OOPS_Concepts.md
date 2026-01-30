# 🏗️ Python Cheat Sheet: OOPS Concepts

## 1. Class vs Object
- **Class**: The Blueprint (General concept: `Dog`).
- **Object/Instance**: The House (Specific case: `my_dog`).

## 2. The Skeleton
```python
class Dog:
    # Class Variable (Shared by all)
    species = "Canine" 
    
    def __init__(self, name):
        # Instance Variable (Unique to each)
        self.name = name 
    
    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Rex")
d.bark()
```

## 3. The 4 Pillars 🏛️
1. **Encapsulation**: Hiding data.
   - `_name` (Protected - Convention)
   - `__name` (Private - Mangled)
2. **Inheritance**: Reuse code.
   - `class Puppy(Dog):`
   - Use `super().__init__()` to call parent constructor.
3. **Polymorphism**: Same method name, different behavior.
   - `cat.speak()` vs `dog.speak()`.
4. **Abstraction**: Hiding complexity.
   - Use `from abc import ABC, abstractmethod`.

## 4. Magic Methods (Dunder)
- `__init__`: Constructor.
- `__str__`: User-friendly string.
- `__repr__`: Developer string.
- `__add__`: Operator overloading (`+`).
- `__len__`: Control `len(obj)`.

## 5. Modern OOPS
- **@property**: Make a method look like a variable (Getters/Setters).
- **@staticmethod**: Utility method (No `self`).
- **@classmethod**: Factory method (Takes `cls`).
- **@dataclass**: Auto-generates `__init__`, `__repr__`, etc.
