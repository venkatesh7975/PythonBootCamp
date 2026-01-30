# 🧮 Python Cheat Sheet: Operators & Math

## 1. Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` **True Division** (Always returns a float: `4/2 = 2.0`)
- `//` **Floor Division** (Chops decimal/rounds down: `5//2 = 2`)
- `%` **Modulus** (Remainder: `10 % 3 = 1`) -> Great for even/odd check.
- `**` **Exponent** (Power: `2 ** 3 = 8`)

## 2. Comparison (Result is always Bool)
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater or equal
- `<=` Less or equal
- `is` Identity check (Same memory address?)
- `in` Membership check (Is item in list/string?)

## 3. Logical Operators
- `and`: Both must be True.
- `or`: At least one is True.
- `not`: Flips the value (`not True` is `False`).

## 4. Assignment Shortcuts
- `x += 5` (Same as `x = x + 5`)
- `x *= 2` (Same as `x = x * 2`)
- Works with all arithmetic operators!

## 5. Math Module Magic
```python
import math
math.ceil(2.1)   # 3 (Always up)
math.floor(2.9)  # 2 (Always down)
math.sqrt(16)    # 4.0
math.pi          # 3.14159...
```
