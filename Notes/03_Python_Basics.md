# 3️⃣ Python Basics: The Toolkit 🧰

Welcome to the **Toolkit**! 🔨 This is where we learn the basic building blocks of Python.

---

## 10. Why Python? 🐍

Why is everyone talking about Python?
1.  **Readable**: `if hungry: eat()` - It's basically English.
2.  **Versatile**: Web Apps 🌐, AI 🤖, Hacking 💻, Automation ⚙️.
3.  **Community**: Need help? Thousands of people are ready to answer on StackOverflow.

---

## 11. Variables: The Name Tags 🏷️

> **Definition**: A variable is a label we give to a value in memory.

### 📦 Analogy: Moving Boxes
Imagine you are moving houses. You have a box full of **Books**.
*   **Variable Name**: The label "Books" written on the box.
*   **Value**: The actual books inside.
*   **Memory**: The corner of the room where the box sits.

In Python:
```python
score = 100
player_name = "Mario"
```
*   We stuck the label `score` on the number `100`.
*   We stuck the label `player_name` on the text `"Mario"`.

> **Rule**: Naming matters! `x = 10` is bad. `age = 10` is good.

---

## 12. Data Types: The Flavors 🍦

Data comes in different flavors. Python detects them automatically!

| Type | Name | Example | Description |
| :--- | :--- | :--- | :--- |
| **Integer** | `int` | `5`, `-10`, `0` | Whole numbers. No decimals. |
| **Float** | `float` | `3.14`, `-0.001` | Decimal numbers. |
| **String** | `str` | `"Hello"`, `'A'` | Text. Must have quotes! |
| **Boolean** | `bool` | `True`, `False` | Yes/No switches. |
| **None** | `NoneType`| `None` | Empty/Null. The void. |

> **Pro Tip**: Use `type(variable)` to check the flavor!
> `type(3.14)` -> `<class 'float'>`

---

## 13. Operators: The Math Gym 🏋️‍♂️

Time to do some heavy lifting!

### ➕ Arithmetic
*   `+` (Add), `-` (Subtract), `*` (Multiply)
*   `/` (Divide): `10 / 2 = 5.0` (Always returns float!)
*   `//` (Floor Div): `10 // 3 = 3` (Chops off the decimal).
*   `%` (Modulus): `10 % 3 = 1` (Remainder).
*   `**` (Power): `2 ** 3 = 8` ($2^3$).

### ⚖️ Comparison
*   `==` (Equal), `!=` (Not Equal)
*   `>`, `<`, `>=`, `<=`

### 🧠 Logical
*   `and`: Both must be True.
*   `or`: At least one must be True.
*   `not`: Reverses it.

---

## 14. Typecasting: The Cosplay 🎭

Changing a value from one type to another.

*   **Int -> Float**: `float(5)` -> `5.0`
*   **Float -> Int**: `int(5.9)` -> `5` (Warning: It doesn't round, it chops!) ✂️
*   **Number -> String**: `str(10)` -> `"10"`
*   **String -> Int**: `int("50")` -> `50` (Only works if the string is a valid number!)

---

## 🕵️‍♂️ Debugging Detective: The Math Mistake

**Scenario**: A student wants to find the average of 2 and 3.
```python
a = 2
b = 3
avg = a + b / 2
print(avg)
```
**Output**: `3.5` ... Wait, (2+3)/2 is 2.5! Why 3.5? 🤔

**❌ The Bug**: Operator Precedence! Division `/` happens before Addition `+`.
It calculated `2 + (3/2)` -> `2 + 1.5` -> `3.5`.

**✅ Fix**: Use parentheses!
`avg = (a + b) / 2`

---

## 🏋️‍♀️ Gym Time: Mental Reps

1.  **Variable Name**: Is `2nd_place` a valid variable name? Why or why not?
2.  **Type Check**: What is the type of `result`?
    ```python
    result = 10 / 2
    ```
    (Trick question!)
3.  **Modulus Magic**: What is `15 % 4`?
4.  **Boolean Logic**: `True and False` -> ?

---

## 🤣 Fun Zone

**Q: Why do programmers confuse Halloween and Christmas?**
**A:** Because `OCT 31 == DEC 25`! 🎃🎄
(Octal 31 equals Decimal 25)

---

## 🏆 Challenge Mode: 20 Practice Problems

### 🧠 Conceptual (Multiple Choice & Short Answer)

1.  **Valid Variable?**: Is `1st_prize` a valid variable name? Why?
2.  **Case Sensitivity**: Are `Score` and `score` the same variable?
3.  **Type Check**: What function do you use to find out if a variable is an Integer or a String?
4.  **Math**: What is the result of `10 / 3` in Python? (Exact output).
5.  **Math**: What is the result of `10 // 3` in Python?
6.  **Comparison**: `5 == "5"` -> True or False?
7.  **Logic**: `True and False` evaluates to?
8.  **Typecasting**: What happens if you run `int("Hello")`?
9.  **Modulo**: What is `20 % 6`?
10. **Convention**: Which variable name is better: `n` or `user_age`?

### 💻 Coding Challenges

11. **Swap**: Write code to swap two variables `a = 5`, `b = 10` so `a` becomes 10 and `b` becomes 5.
12. **Circle Area**: Calculate area of a circle where `radius = 5` and `pi = 3.14159`. Print it.
13. **F to C**: Convert 100°F to Celsius. Formula: `(F - 32) * 5/9`.
14. **Quadratic**: Calculate `x` for `y = ax^2 + bx + c` where `a=2, b=3, c=1, x=5`.
15. **Even/Odd (No If)**: Use Modulo `%` to find the remainder of `17` divided by `2`.
16. **Power**: Calculate `2` to the power of `10`.
17. **Casting**: Convert the float `9.99` to an integer. What is the value?
18. **Logic Puzzle**: `(5 > 3) and (2 < 4) or (not True)`. What is the result?
19. **Remainder**: Distribute 100 apples to 3 people. How many are left over?
20. **String Math**: What is `"10" + "10"`?

<details>
<summary><strong>⬇️ Click to Reveal Solutions</strong></summary>

**Conceptual Answers**
1. No. Cannot start with a number.
2. No. Python is case-sensitive.
3. `type()`.
4. `3.3333333333333335` (Float).
5. `3` (Integer).
6. False. Int is not equal to String.
7. False.
8. `ValueError`.
9. 2.
10. `user_age` (More descriptive).

**Coding Answers**
11. `temp = a; a = b; b = temp` OR `a, b = b, a`.
12. `area = 3.14159 * (5 ** 2)` -> `78.53975`.
13. `(100 - 32) * 5/9` -> `37.77...`.
14. `2*(5**2) + 3*5 + 1` -> `50 + 15 + 1` -> `66`.
15. `17 % 2` -> `1` (It is Odd).
16. `2 ** 10` -> `1024`.
17. `int(9.99)` -> `9`.
18. `True and True or False` -> `True`.
19. `100 % 3` -> `1`.
20. `"1010"` (String Concatenation).
</details>

---
**Next Up:** We learn how to handle text with **Strings**! 🧵
