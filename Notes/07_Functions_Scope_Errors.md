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

---

## 26. Arguments Masterclass 🤹‍♀️

Functions are flexible! Here is how to pass data like a pro.

### 1. Positional vs Keyword Arguments
*   **Positional**: Order matters. `func(10, 20)`
*   **Keyword**: Name matters. `func(b=20, a=10)` (Order doesn't matter!)

### 2. Default Arguments 🛡️
If the user forgets to send data, use a backup value.
```python
def greet(name="User"):
    print(f"Hello, {name}")

greet("Alice") # "Hello, Alice"
greet()        # "Hello, User" (Backup used!)
```

### 3. *args & **kwargs (The Wildcards) 🃏
What if you don't know how many arguments are coming?
*   `*args`: Collects extra positional arguments into a **Tuple**.
*   `**kwargs`: Collects extra keyword arguments into a **Dictionary**.

```python
def party(*args, **kwargs):
    print(args)   # ('Pizza', 'Coke')
    print(kwargs) # {'location': 'Home', 'time': '8pm'}

party("Pizza", "Coke", location="Home", time="8pm")
```

### 4. Docstrings 📜
Documentation for your function. It helps other coders (and future you) understand what it does.
```python
def square(n):
    """
    Takes a number n and returns its square.
    """
    return n**2
```
> **Tip**: Hover over the function in VS Code to see this text!

---

## 27. Lambda Functions: The Speedster ⚡

> **Definition**: A small, anonymous function defined in one line.

**Syntax**: `lambda arguments : expression`

**Example**:
```python
# Normal
def add(x, y):
    return x + y

# Lambda
add_lambda = lambda x, y : x + y

print(add_lambda(5, 3)) # 8
```
**When to use?** Inside other functions like `map()` or `filter()`.
`list(map(lambda x: x*2, [1, 2, 3]))` -> `[2, 4, 6]`

---

## 28. Scope: The House Rules 🏠

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

## 29. Exception Handling: The Airbag 🚗

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

---

## 30. Recursion & The Call Stack 🔄�

> **Definition**: When a function calls *itself* to solve a smaller version of the problem.

### 🥞 Analogy 1: The Call Stack (Stack of Plates)
Imagine a stack of plates.
1.  **Push**: You put a plate on top.
2.  **Pop**: You can only remove the *top* plate.
3.  **LIFO**: Last In, First Out.

When functions call other functions, Python stacks them up.
*   `main()` calls `A()` -> `A` goes on top of `main`.
*   `A()` calls `B()` -> `B` goes on top of `A`.
*   `B()` finishes -> `B` is popped off. We go back to `A`.

### 🪆 Analogy 2: recursion (Russian Dolls)
Opening a Russian Doll.
1.  **The Base Case**: The smallest solid doll in the center. (Stop opening!)
2.  **The Recursive Step**: Opening a doll to find a smaller one inside.

**Example: Factorial (5!)**
`5! = 5 * 4 * 3 * 2 * 1`
`factorial(5) = 5 * factorial(4)`

```python
def factorial(n):
    # 1. Base Case (The smallest doll)
    if n == 1:
        return 1
    
    # 2. Recursive Step (Opening the doll)
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120
```

> **⚠️ Danger Zone**: **RecursionError**.
> If you forget the *Base Case*, the function calls itself forever (Infinite Loop) until the stack overflows! 💥

---

## 31. Debugging Detective: The Shadow

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
---

## 🏆 Challenge Mode: 20 Practice Problems

### 🧠 Conceptual (Multiple Choice & Short Answer)

1.  **Definition**: What keyword defines a function?
2.  **Parameters**: In `def foo(x):`, what is `x` called? (Argument or Parameter?)
3.  **Scope**: If you define `x` inside a function, can you use it outside?
4.  **Keyword**: What keyword allows a function to modify a Global variable?
5.  **Return**: What does a function return if there is no `return` statement?
6.  **Error Handling**: Which block catches the error? `try` or `except`?
7.  **Args**: What data type does `*args` collect arguments into? (List or Tuple?)
8.  **Recursion**: What handles the "Stop Condition" in recursion?
9.  **Stack**: What structure tracks function calls? (Queue or Stack?)
10. **Infinity**: What error occurs if a recursive function has no base case?

### 💻 Coding Challenges

11. **Hello**: Write a function `greet(name)` that prints "Hello, [name]".
12. **Add**: Write `add(a, b)` that returns the sum of a and b.
13. **Square**: Write `square(n)` that returns $n^2$.
14. **Check Even**: Write `is_even(n)` that returns `True` if even, `False` if odd.
15. **Scope Test**: Fix this:
    ```python
    def test():
        msg = "Hi"
    print(msg) # Error
    ```
16. **Sum All**: Write `sum_all(*args)` that sums ANY number of arguments.
17. **Factorial**: Write a recursive function for factorial (or copy the example!).
18. **Countdown (Recursive)**: Write `count_down(n)` that prints n, n-1... 1, "Go!".
19. **Default Arg**: Write `greet(name="User")` so it works even without an argument.
20. **Lambda**: (Advanced) Write a lambda function that adds 10 to a number.

<details>
<summary><strong>⬇️ Click to Reveal Solutions</strong></summary>

**Conceptual Answers**
1. `def`.
2. Parameter. (Value sent is Argument).
3. No (Local Scope).
4. `global`.
5. `None`.
6. `except`.
7. Tuple.
8. Base Case.
9. Stack.
10. `RecursionError`.

**Coding Answers**
11. `def greet(n): print(f"Hello, {n}")`.
12. `def add(a,b): return a+b`.
13. `def square(n): return n**2`.
14. `def is_even(n): return n % 2 == 0`.
15. `msg` is local. Can't print it outside. Return it instead.
16. `def sum_all(*args): return sum(args)`.
17. See notes.
18. `if n=0: print("Go!") else: print(n); count_down(n-1)`.
19. `def greet(name="User"): ...`.
20. `add_10 = lambda x: x + 10`.
</details>

---

**Next Up:** The Grand Finale... **Object Oriented Programming**! 🏗️
