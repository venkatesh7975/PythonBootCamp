# 7️⃣ Functions & Errors: The Safety Net 🛡️

Welcome to **The Safety Net**! 🕸️ Here we learn how to make re-usable tools and how to stop our code from crashing and burning.

---

## 25. Functions: The Magic Box 📦

> **Definition**: A reusable block of code that does *one thing* well.

### 🍹 Analogy: The Blender
*   **Input**: Fruit 🍓 (Arguments)
*   **Process**: Whirrrr! 🌀 (Function Body)
*   **Output**: Juice 🥤 (Return Value)

**Why use them?**
Instead of chopping fruit by hand 100 times, you just push the button on the blender.

**Syntax**:
```python
def make_juice(fruit):
    return f"{fruit} Juice"
```

> **Return vs Print**:
> *   `print()`: Showing a picture of the juice. 🖼️
> *   `return`: Hands you the *actual* glass of juice. 🍹

---

## 26. Scope: The House Rules 🏠

> **Definition**: Where a variable lives.

### 🌎 Analogy: Local vs Global
1.  **Local (Bedroom)**: Things inside your room (Function) are *yours*. Your mom (Global) can't see them unless you bring them out.
2.  **Global (Living Room)**: Things in the living room are for *everyone*.

```python
x = "Global"

def my_room():
    y = "Local"
    print(x) # Works! (Can see living room)
    print(y) # Works!

print(y) # CRASH! 💥 (Can't see inside bedroom)
```

---

## 27. Exception Handling: The Airbag 🚗

> **Definition**: Catching errors before they crash the program.

### 🛑 Analogy: Driving a Car
*   **Normal Code**: Driving smoothly.
*   **Error**: Hitting a pothole. 🕳️
*   **Crash**: Car is destroyed. Game Over. ☠️
*   **Exception Handling**: Airbag deploys! You are safe. You fix the tire and keep driving. 🔧

**Syntax**:
```python
try:
    # Risky Code
    print(10 / 0)
except ZeroDivisionError:
    # Safety Net
    print("You can't divide by zero, silly!")
```

**Keywords**:
*   `try`: "Attempt this."
*   `except`: "If it creates a fireball, do this instead."
*   `finally`: "Do this no matter what happens." (Cleanup) 🧹

---

## 🕵️‍♂️ Debugging Detective: The Shadow

**Scenario**:
```python
x = 10

def change_x():
    x = 20 # Does this change global x?

change_x()
print(x)
```
**Output**: `10` ... Wait, why didn't it change to 20? 😲
**The Detective**: The function created a *new local* variable named `x`. It didn't touch the global one!
**Fix**: Use `global x` inside the function if you *really* want to change the global one. (But don't do this often!)

---

## 🏋️‍♀️ Gym Time: Mental Reps

1.  **Function Fun**: Write a function `double(n)` that takes a number and returns it multiplied by 2.
2.  **Scope Scope**: Can a function read a global variable? Can the main program read a local variable?
3.  **Crash Test**: Wrap this code in a try-except block so it doesn't crash if user types text instead of a number.
    ```python
    age = int(input("Enter age: "))
    ```

---

## 🤣 Fun Zone

**Q: Why do Java programmers wear glasses?**
**A:** Because they don't C#! (Wait, I used that one... 😅)

**Q: A SQL query walks into a bar, walks up to two tables and asks...**
**A:** "Can I join you?" 👫

---
**Next Up:** The Grand Finale... **Object Oriented Programming**! 🏗️
