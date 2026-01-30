# 🚦 Python Cheat Sheet: Control Flow

## 1. Conditions (`if / elif / else`)
```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Study harder!")
```
- **Ternary (One-liner)**: `status = "Pass" if score > 50 else "Fail"`

## 2. Iteration (Loops)
- **FOR Loop**: Used when you know the number of steps.
  - `for i in range(5):` (0 to 4)
  - `for item in list:` (Direct iteration)
- **WHILE Loop**: Used as long as a condition is True.
  - `while energy > 0:`

## 3. Loop Control
- `break`: Eject from the loop immediately.
- `continue`: Skip the rest of CURRENT iteration and go to next.
- `pass`: Do nothing (placeholder).

## 4. Range Function
- `range(5)` -> 0, 1, 2, 3, 4
- `range(2, 5)` -> 2, 3, 4
- `range(0, 10, 2)` -> 0, 2, 4, 6, 8 (Step = 2)

## 5. Truthiness
Everything has a boolean value:
- **FALSE**: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`.
- **TRUE**: Almost everything else!
```python
if my_list: # Checks if list is NOT empty
    print("Items found!")
```
