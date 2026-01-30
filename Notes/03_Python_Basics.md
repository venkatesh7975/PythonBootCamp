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
**Next Up:** We learn how to handle text with **Strings**! 🧵
