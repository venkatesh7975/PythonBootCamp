# 🐛 Python Cheat Sheet: Error Handling

## 1. The Block Structure
```python
try:
    # Code that might crash
    res = 10 / 0
except ZeroDivisionError:
    # Runs ONLY if specific error happens
    print("Can't do that!")
except Exception as e:
    # Generic catch-all
    print(f"Error: {e}")
else:
    # Runs ONLY if NO error happened
    print("Success!")
finally:
    # ALWAYS runs (Cleanup)
    print("Cleaning up...")
```

## 2. Raising Exceptions
- **Force an error**: `if x < 0: raise ValueError("Positive only!")`
- **Re-raise**: Use `raise` inside an `except` block.

## 3. Custom Exceptions
```python
class MyCustomError(Exception):
    pass

raise MyCustomError("System Overload!")
```

## 4. Assertion (Debugging Only)
- `assert x > 0, "x should be positive"`
- If condition is False, raises `AssertionError`.
- **Note**: Assertions can be disabled in production!

## 5. Common Error Types
| Type | Cause |
|------|-------|
| **SyntaxError** | Typos, missing colons. |
| **NameError** | Using a variable that isn't defined. |
| **TypeError** | `5 + "hi"` (Math on incompatible types). |
| **ValueError** | `int("abc")` (Right type, wrong value). |
| **IndexError** | `L[99]` (Index out of range). |
| **KeyError** | `d["missing"]` (Key not in dict). |
