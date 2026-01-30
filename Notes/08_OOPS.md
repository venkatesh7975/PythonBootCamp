# 8️⃣ OOPS: The Blueprint 🏗️

Welcome to **The Architect's Studio**! 📐 This is where we stop writing "scripts" and start building "systems".

---

## 28. OOPS Concepts: The Master Plan 🗺️

> **Definition**: Modeling real-world things in code.

### 🏠 Analogy: The Blueprint & The House
*   **Class (Blueprint)**: The drawing on paper. You can't live in it. It just says "3 Bedrooms". 📝
*   **Object (House)**: The actual building made from the drawing. You can build 50 houses from 1 blueprint. 🏡
*   **Instance**: A specific house (e.g., "Number 12, Maple Street").

**The Code**:
```python
class Dog:
    pass

buddy = Dog() # Create a new Dog object
max = Dog()   # Create another Dog object
```

---

### Constructor (`__init__`): The Factory Line 🏭

When a car is born, it needs tires and paint *before* it leaves the factory.
The `__init__` method runs **automatically** when you create an object.

**Syntax**:
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Set name
        self.breed = breed # Set breed

d1 = Dog("Simba", "Lion")
```

> **Note**: `self` is how the object refers to *itself*.
> "My name is Simba" -> `self.name = "Simba"`

---

### Instance Variables: The DNA 🧬

Data that makes *this* object unique.
*   `d1.name` -> `"Simba"`
*   `d2.name` -> `"Nala"`

They share the same Code (Class), but have different Data (Instance Variables).

---

## 🕵️‍♂️ Debugging Detective: The Missing Self

**Scenario**:
```python
class Cat:
    def meow(): # Missing something?
        print("Meow!")

c = Cat()
c.meow()
```
**Error**: `TypeError: meow() takes 0 positional arguments but 1 was given` ❌
**Why?**: When you call `c.meow()`, Python secretly passes `c` as the first argument! It becomes `Cat.meow(c)`.
**Fix**: Add `self`!
`def meow(self):`

---

## 🏋️‍♀️ Gym Time: Mental Reps

1.  **Blueprint Basics**: Create a class `Car`.
2.  **Constructor Challenge**: Add an `__init__` method to `Car` that takes `color` and `brand`.
3.  **Self-Awareness**: Why do we need `self`? What happens if we remove it from `def drive(self):`?
4.  **Instantiation**: Create 2 cars: A "Red Toyota" and a "Blue Honda".

---

## 🤣 Fun Zone

**Q: Why did the Object-Oriented Programmer get rich?**
**A:** Because they had **Class**! 🎩💰

**Q: How do you comfort a JavaScript bug?**
**A:** You `console` it! (Okay, wrong language, but still funny).

---
---

## 🏆 Challenge Mode: 20 Practice Problems

### 🧠 Conceptual (Multiple Choice & Short Answer)

1.  **Analogy**: If Class is the "Blueprint", what is the Object?
2.  **Terminology**: What is an "Instance"?
3.  **Keyword**: What keyword defines a Class?
4.  **Constructor**: What is the name of the method that runs automatically?
5.  **Self**: What does `self` represent?
6.  **Attribute**: In `self.name = "Rex"`, what is `name`?
7.  **Method**: What do we call a function inside a class?
8.  **Inheritance**: Can a child class inherit methods from a parent class?
9.  **Polymorphism**: Can different classes have a method with the same name?
10. **Convention**: Should Class names be `lowercase` or `Capitalized`?

### 💻 Coding Challenges

11. **Define**: Define an empty class named `Robot`.
12. **Init**: Add an `__init__` that sets `self.model`.
13. **Object**: Create an object `r1` of class `Robot` with model "RX-78".
14. **Method**: Add `speak(self)` that prints "I am [model]".
15. **Access**: Print the `model` of `r1` directly.
16. **Change**: Change the `model` of `r1` to "Gundam".
17. **Attributes**: Add `self.battery = 100` to `__init__` (default value).
18. **Logic**: Write `drain(self)` that decreases battery by 10.
19. **Inheritance**: Create `class Android(Robot):` that inherits from Robot.
20. **Override**: Add `speak(self)` to Android that says "Hello Human" instead.

<details>
<summary><strong>⬇️ Click to Reveal Solutions</strong></summary>

**Conceptual Answers**
1. The House / The actual thing.
2. A specific object created from the class.
3. `class`.
4. `__init__`.
5. The object itself (current instance).
6. Instance Variable (Attribute).
7. Method.
8. Yes.
9. Yes.
10. `Capitalized` (PascalCase).

**Coding Answers**
11. `class Robot: pass`.
12. `def __init__(self, model): self.model = model`.
13. `r1 = Robot("RX-78")`.
14. `def speak(self): print(f"I am {self.model}")`.
15. `print(r1.model)`.
16. `r1.model = "Gundam"`.
17. `self.battery = 100`.
18. `def drain(self): self.battery -= 10`.
19. `class Android(Robot): pass`.
20. `def speak(self): print("Hello Human")`.
</details>

---

**🎓 The End!** You have completed the Python Bootcamp Notes! Now go build something awesome! 🚀
