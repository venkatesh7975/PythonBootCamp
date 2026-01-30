# 🐍 Python Cheat Sheet: Basics & Variables

## 1. The Core 3
- **ID**: `id(obj)` - Memory address (The "where").
- **TYPE**: `type(obj)` - Data category (The "what").
- **VALUE**: The data itself (The "content").

## 2. Variables (Sticky Notes 🏷️)
- **Rules**: Start with letter/underscore, no spaces, CASE SENSITIVE.
- **Snake Case**: `my_variable_name` (Standard).
- **Multiple Assignment**: `x, y, z = 1, 2, 3`
- **Dynamic Typing**: `x = 10` then `x = "Hi"` is legal!

## 3. Data Types (The Big 4)
| Type | Example | Description |
|------|---------|-------------|
| **int** | `10`, `-5` | Whole numbers. |
| **float** | `3.14`, `2.0` | Decimal numbers. |
| **str** | `"Hi"`, `'Yo'` | Text data. |
| **bool** | `True`, `False` | Logic (Capital T/F). |
| **None** | `None` | Absence of value. |

## 4. Input & Output
- **Print**: `print("Hi", end=" ")` (Stay on line), `print(a, b, sep="|")` (Custom separator).
- **Input**: `val = input("Enter: ")` (**Always returns a string!**)
- **Casting**: `int("10")`, `str(5)`, `float("3.5")`, `bool(1)`.

## 5. Useful Built-ins
- `len(s)`: Length of item.
- `help(obj)`: Show documentation.
- `dir(obj)`: Show available methods.
