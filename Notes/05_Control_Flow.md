# 5️⃣ Control Flow & Inputs: The Traffic Cop 🚦

Welcome to the **Traffic Control Center**! 🛑 Without control flow, code just runs from top to bottom like a waterfall. We want it to be smart!

---

## 18. Conditional Statements: The Crossroads 🛣️

> **Definition**: Making decisions based on logic.

### 🚦 Analogy: The Red Light
*   **Green**: Go! (Execute Code)
*   **Red**: Stop! (Skip Code)

**Structure**:
```python
if hungry:
    eat_pizza()
elif tired:
    sleep()
else:
    work()
```

> **Nested If**: An `if` inside an `if`. Like a Russian Doll 🪆.
> "If it's raining outside... AND if I have an umbrella..."

---

## 19. Loops: The Treadmill 🏃

> **Definition**: Doing the same thing over and over.

### 🔁 Analogy: Listening to a Song on Repeat
1.  **For Loop**: Plays the song *5 times* then stops. (Counted)
2.  **While Loop**: Plays the song *until* you say "Stop". (Condition)

**The Toolkit**:
*   `break`: EMERGENCY STOP! 🚨 Jump out of the loop immediately.
*   `continue`: Skip this song, play the next one. ⏭️
*   `pass`: Do nothing. Just chil. 🧘

---

## 20. Reading Inputs: The Interview 🎤

Code is boring if it doesn't talk back. Here is the **Ultimate Guide to Input**.

> **The Golden Rule**: `input()` varies depending on Python version, but in Python 3, it **ALWAYS returns a String**.

### 🛠️ Common Scenarios

#### 1. The Simple String (Name, City)
```python
name = input("Enter your name: ")
# user input: Alice
# name = "Alice"
```

#### 2. The Integer / Float (Age, Price) 🔢
You **must** cast it. If you don't, math will fail.
```python
age = int(input("Enter age: "))
price = float(input("Enter price: "))
```
> **⚠️ Error Alert**: `ValueError`.
> If user types `"Twenty"` instead of `20`, the program crashes!

#### 3. Two Values on One Line (Coordinates) 📍
User types: `10 20`
```python
a, b = map(int, input().split())
```
*   `input()` -> `"10 20"` (String)
*   `split()` -> `["10", "20"]` (List of Strings)
*   `map(int, ...)` -> `10, 20` (Integers)
*   `a, b` -> Assigns 10 to a, 20 to b.

#### 4. A List of Numbers (Array) 📜
User types: `1 2 3 4 5`
```python
nums = list(map(int, input().split()))
# nums = [1, 2, 3, 4, 5]
```

#### 5. Multiple Lines of Input (Test Cases) 🔁
Competitive programming often asks for `T` test cases.
```python
T = int(input()) # Number of test cases
for _ in range(T):
    n = int(input())
    print(n * 2)
```

### 🚫 Common Errors & Fixes

| Scenario | Code | Error | Why? |
| :--- | :--- | :--- | :--- |
| **Math on Strings** | `"5" + 5` | `TypeError` | Can't add Text to Number. |
| **Bad Cast** | `int("Hello")` | `ValueError` | "Hello" is not a number. |
| **Not Enough Input** | `x, y = input().split()` | `ValueError` | User only typed one value. |

---

## 🕵️‍♂️ Debugging Detective: The Infinite Nightmare

**Scenario**:
```python
n = 5
while n > 0:
    print(n)
    # n never changes!
```
**Problem**: The condition `n > 0` is ALWAYS True because `n` stays 5 forever.
**Result**: Your computer freezes. ❄️
**Fix**: Add `n -= 1` inside the loop!

---

## 🏋️‍♀️ Gym Time: Mental Reps

1.  **The Bouncer**: Write an `if` statement that checks if `age >= 18`. If yes, print "Enter". Else, "Go home".
2.  **Loop De Loop**: Write a loop that prints even numbers from 0 to 10.
3.  **Input Issues**:
    ```python
    x = input()
    y = input()
    print(x + y)
    ```
    If user types `5` and `5`, what prints? `10` or `55`?
4.  **The Multi-Tasker**: Write code to read three numbers from a single line (like `10 20 30`) and print their sum. Hint: Use `split()`.

---

## 🤣 Fun Zone

**Q: A programmer's wife asks:**
"Go to the store and buy a loaf of bread. If they have eggs, buy a dozen."
**A:** The programmer comes back with 12 loaves of bread.
**Why?** Because they had eggs! 🥚🍞

---

## 🏆 Challenge Mode: 20 Practice Problems

### 🧠 Conceptual (Multiple Choice & Short Answer)

1.  **Input Type**: What type does `input()` always return in Python 3?
2.  **Cast**: How do you turn string `"5"` into an integer?
3.  **Condition**: `if x > 10: print("A")`. What prints if `x = 10`?
4.  **Loop**: Does a `while` loop run 0, 1, or Infinite times if the condition is initially False?
5.  **Break**: What keyword stops a loop immediately?
6.  **Skip**: What keyword skips the rest of the loop and starts the next iteration?
7.  **Syntax**: Does `if` statement need parentheses around the condition? (e.g., `if (x>5):`)
8.  **Elif**: Can you have an `elif` without an `if`?
9.  **Range**: `range(5)` produces what numbers?
10. **Error**: What error stops execution when you try to use a variable that hasn't been defined?

### 💻 Coding Challenges

11. **Age Check**: Write code that asks for age. If `<18` print "Minor", else "Adult".
12. **Print 1-10**: Use a for loop to print numbers 1 to 10.
13. **Countdown**: Use a while loop to print 5, 4, 3, 2, 1, "Blastoff!".
14. **Even Numbers**: Print all even numbers between 1 and 20.
15. **Sum Input**: Ask user for 2 numbers and print their sum. (Remember to cast!).
16. **Password**: Keep asking "Enter Password" *while* the input is not equal to "secret".
17. **Grade**: `score > 90` -> "A", `> 80` -> "B", else "C". Write the logic.
18. **Table**: Print the multiplication table of 5 (5, 10, 15... 50).
19. **List Sum**: Given list `L = [10, 20, 30]`, use a loop to find the sum.
20. **Max**: Ask user for 2 numbers, print the larger one.

<details>
<summary><strong>⬇️ Click to Reveal Solutions</strong></summary>

**Conceptual Answers**
1. String (`str`).
2. `int("5")`.
3. Nothing (10 is not greater than 10).
4. 0 times.
5. `break`.
6. `continue`.
7. No. Parentheses are optional in Python.
8. No.
9. `0, 1, 2, 3, 4`.
10. `NameError`.

**Coding Answers**
11. `if int(input()) < 18: print("Minor") else: print("Adult")`.
12. `for i in range(1, 11): print(i)`.
13. `n=5; while n>0: print(n); n-=1; print("Blastoff!")`.
14. `for i in range(2, 21, 2): print(i)`.
15. `print(int(input()) + int(input()))`.
16. `while input() != "secret": pass`.
17. `if s > 90: "A" elif s > 80: "B" else: "C"`.
18. `for i in range(1, 11): print(5 * i)`.
19. `total=0; for x in L: total+=x`.
20. `a,b = map(int, input().split()); if a>b: print(a) else: print(b)`.
</details>

---
**Next Up:** We organize our messy data with **Data Structures**! 📚
