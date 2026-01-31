# Debugging and Error Handling in Python

Understanding errors is a crucial part of becoming a proficient programmer. In Python, errors are generally categorized into three types: **Syntax Errors**, **Runtime Errors (Exceptions)**, and **Logical Errors**.

---

## 1. Syntax Errors
Syntax errors occur when the Python interpreter cannot understand your code because it violates the grammar rules of the language. These errors prevent the program from starting at all.

| Error Type | What it is | Real-World Scenario | How to Fix |
| :--- | :--- | :--- | :--- |
| **Missing Colon** | Forgetting `:` after `if`, `for`, `def`, etc. | Quick typing or switching from C++/Java. | Add `:` at the end of control statements. |
| **Unmatched Brackets**| Opening `(` or `[` but forgetting to close it. | Long print statements or math formulas. | Ensure every opener has a closer. |
| **Indentation Error** | Inconsistent spacing (Python groups code by space). | Copy-pasting code or mixing tabs/spaces. | Use 4 spaces per level consistently. |
| **Invalid Keyword** | Misspelling keywords (e.g., `forr` instead of `for`). | Simple typos during coding. | Check keyword spelling against documentation. |
| **Assignment in If** | Using `=` instead of `==` in a condition. | Trying to check a user's role/status. | Use `==` for comparison, `=` for assignment. |
| **Invalid Identifier**| Variable names starting with numbers (e.g., `1st_place`). | Naming variables without following rules. | Start names with letters or underscores. |
| **Mismatched Quotes**| Mixing `'` and `"` for a single string. | Inconsistent string definition. | Use the same quote type for start and end. |

---

## 2. Runtime Errors (Exceptions)
Runtime errors occur while the program is executing. The syntax is correct, but something happens that Python can't handle (e.g., dividing by zero). These are known as **Exceptions**.

| Exception Name | When it Happens | SCENARIO |
| :--- | :--- | :--- |
| **ZeroDivisionError** | Dividing a number by 0. | A calculator app where the user inputs 0 as divisor. |
| **TypeError** | Operating on incompatible types. | Adding a string `"10"` and an integer `5`. |
| **ValueError** | Correct type but inappropriate value. | Converting a non-numeric string `"hello"` to `int`. |
| **NameError** | Using a variable that isn't defined. | Misspelling a variable name after defining it. |
| **IndexError** | Accessing a list index that doesn't exist. | Accessing the 10th item in a 3-item list. |
| **KeyError** | Looking for a missing key in a dictionary. | Searching for "email" in a profile that only has "name". |
| **AttributeError** | Calling a method that doesn't exist for an object.| Trying to `.append()` to an integer. |
| **ModuleNotFoundError**| Importing a module that isn't installed. | Typos in `import` (e.g., `import pands`). |
| **FileNotFoundError** | Opening a file that doesn't exist. | Reading `data.txt` before it's created. |
| **OverflowError** | Calculation exceeds numeric limits. | Calculating an extremely large exponent. |
| **RecursionError** | Infinite recursion (missing base case). | A function that calls itself forever. |
| **StopIteration** | Iterator has no more items. | Stepping past the end of a list manually. |
| **AssertionError** | An `assert` condition fails. | Validating input (e.g., age must be > 0). |
| **NotImplementedError**| Calling an abstract method not yet overridden. | A base class feature not yet built in a subclass. |

---

## 3. Logical Errors (Bugs)
Logical errors are the most dangerous because the program runs without crashing but produces the **wrong results**.

- **Off-by-one Error**: Miscalculating loop ranges (e.g., `range(5)` vs `range(1, 6)`).
- **Operator Precedence**: Forgetting math order (PEMDAS). Example: `10 + 20 / 2` is `20`, but `(10 + 20) / 2` is `15`.
- **Scoping Issues**: Mistakenly creating a local variable inside a function when you meant to update a global one.
- **Truthy Trap**: Using `if x == "A" or "B":` which is always true because `"B"` is truthy. Correct is `if x in ["A", "B"]:`.

---

## 4. Handling Errors Gracefully
Instead of letting your program crash, use `try-except` blocks.

```python
try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    # Plan B: Handle the specific error
    print("Oops! You can't divide by zero.")
else:
    # Runs if NO error happened
    print("Everything went smoothly!")
finally:
    # Runs NO MATTER WHAT (Cleanup)
    print("Shutting down the operation.")
```

> [!TIP]
> Always try to catch **specific** exceptions (like `ZeroDivisionError`) rather than using a broad `except Exception:` whenever possible. This helps you identify exactly what went wrong.
