# 4️⃣ Strings & Code Structure: The Text Master 📜

Welcome to the **Text Master** class! ✍️ Most of the web is text (`HTML`, `JSON`, `URLs`). Mastering strings is mastering the web.

---

## 15. String Indexing: The Train 🚆

> **Definition**: Accessing a single character by its position.

### 🎫 Analogy: Reserved Seating
Imagine a string is a train with numbered seats.

**The Train**: `"PYTHON"`

| P | Y | T | H | O | N |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 2 | 3 | 4 | 5 | (Positive) |
| -6 | -5 | -4 | -3 | -2 | -1 | (Negative) |

*   `s[0]` -> **P** (First Car)
*   `s[-1]` -> **N** (Caboose/Last Car)

> **Common Error**: `IndexError`.
> `s[10]` -> The train only has 6 seats! You fell off! 😵

---

## 16. String Slicing: The Cake Cutter 🍰

> **Definition**: Grabbing a *chunk* of text.

**Formula**: `[Start : Stop : Step]`
*   **Start**: Include this index.
*   **Stop**: Stop *before* this index (Exclusive).
*   **Step**: Jump size (Default 1).

**Examples**:
`s = "PYTHON"`

1.  **The Slice**: `s[0:2]` -> `"PY"` (Indices 0, 1. Stop at 2).
2.  **The Open Ended**: `s[2:]` -> `"THON"` (Start at 2, go to end).
3.  **The Backwards Walk**: `s[::-1]` -> `"NOHTYP"` (Reverse the string).

> **Pro Tip**: `s[:]` makes a copy of the whole string!

---

## 17. Code Blocks & Indentation: The Traffic Rules 🚦

In other languages (C, Java), we use `{}` curly braces.
In Python, we use **Space**.

> **Definition**: Indentation defines which lines belong together.

### 🌳 Analogy: The Family Tree
*   **Parent** (Ends with `:`)
    *   **Child** (Indented 4 spaces)
    *   **Child** (Indented 4 spaces)
*   **Neighbor** (Not indented, lives next door)

**Correct**:
```python
if True:
    print("I am inside!")
print("I am outside!")
```

**Wrong**:
```python
if True:
print("Where do I belong??") # IndentationError!
```

> **Rule**: Use **4 Spaces** (or 1 Tab). Don't mix them!

---

## 🕵️‍♂️ Debugging Detective: The Off-By-One Error

**Scenario**: You want the first 3 letters of `"APPLE"`.
```python
fruit = "APPLE"
sliced = fruit[0:2] # Indices 0, 1
print(sliced)
```
**Output**: `AP`
**Expected**: `APP`

**❌ The Bug**: Slicing stops *before* the end index. `[0:2]` gives indices 0 and 1.
**✅ Fix**: You need index 2 included, so stop at 3.
`sliced = fruit[0:3]` -> `APP`

---

## 🏋️‍♀️ Gym Time: Mental Reps

1.  **Index Master**: Given `s = "BOOTCAMP"`, what is `s[-2]`?
2.  **Slicing Challenge**: Extract `"gram"` from `"Programming"`.
3.  **Reversal**: How do you reverse the string `"racecar"`?
4.  **Block Party**:
    ```python
    x = 10
    if x > 5:
        print("A")
    print("B")
    ```
    What prints? `A`? `B`? Or both?

---

## 🤣 Fun Zone

**Q: Why do Python programmers wear glasses?**
**A:** Because they can't **C#**! 🤓

---
**Next Up:** We learn decision making with **Control Flow**! 🚦
