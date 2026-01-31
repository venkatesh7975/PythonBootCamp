"""
02_runtime_errors.py - Understanding Runtime Errors (Exceptions)

Runtime errors occur while the program is running, even if the syntax is correct.
These are also known as "Exceptions". The program "excepts" (diverges) from 
the normal flow because it encountered something it couldn't handle.
"""

print("--- Runtime Errors Demo ---\n")

def demonstrate_error(error_name, code_block):
    """Safely runs code to show what error it produces."""
    print(f"Testing for: {error_name}")
    try:
        code_block()
    except Exception as e:
        print(f"CAUGHT ERROR: {type(e).__name__}")
        print(f"EXPLANATION: {e}\n")

# 1. ZeroDivisionError
# WHEN: Trying to divide a number by 0.
# SCENARIO: A calculator app where a user inputs 0 as the divisor.
demonstrate_error("ZeroDivisionError", lambda: 10 / 0)

# 2. TypeError
# WHEN: Performing an operation on incompatible types.
# SCENARIO: Trying to add a string ("5") and an integer (10) together.
demonstrate_error("TypeError", lambda: "10" + 5)

# 3. ValueError
# WHEN: A function receives an argument of the correct type but inappropriate value.
# SCENARIO: Converting user input "ABC" into an integer using int().
demonstrate_error("ValueError", lambda: int("hello"))

# 4. NameError
# WHEN: Using a variable name that hasn't been defined yet.
# SCENARIO: A typo in a variable name (e.g., 'price' vs 'prcie').
demonstrate_error("NameError", lambda: undefined_variable + 1)

# 5. IndexError
# WHEN: Accessing a list index that is out of range.
# SCENARIO: A list has 3 items, but you try to access the 10th item.
demonstrate_error("IndexError", lambda: [1, 2, 3][10])

# 6. KeyError
# WHEN: Looking up a key in a dictionary that doesn't exist.
# SCENARIO: Searching for "email" in a user profile that only has "name".
demonstrate_error("KeyError", lambda: {"name": "Alice"}["age"])

# 7. AttributeError
# WHEN: Trying to access an attribute or method that doesn't exist for that object.
# SCENARIO: Trying to use .append() (which is for lists) on an integer.
demonstrate_error("AttributeError", lambda: (10).append(5))

# 8. ModuleNotFoundError
# WHEN: Trying to import a module that isn't installed or doesn't exist.
# SCENARIO: Mistyping 'pandas' as 'pands'.
demonstrate_error("ModuleNotFoundError", lambda: __import__("non_existent_module"))

# 9. FileNotFoundError
# WHEN: Trying to open a file that doesn't exist in the specified path.
# SCENARIO: Forgetting to create 'data.txt' before reading it.
demonstrate_error("FileNotFoundError", lambda: open("ghost_file.txt", "r"))

# 10. OverflowError
# WHEN: A calculation exceeds the maximum limit for a numeric type (less common with Python ints, but happens in math library).
# SCENARIO: Calculating an extremely large exponent.
import math
demonstrate_error("OverflowError", lambda: math.exp(1000))

# 11. RecursionError
# WHEN: A function calls itself too many times, exceeding the maximum recursion depth.
# SCENARIO: A recursive function that forgets its "base case" (where to stop).
def infinite_recursion():
    return infinite_recursion()
demonstrate_error("RecursionError", lambda: infinite_recursion())

# 12. StopIteration
# WHEN: The next() function is called on an iterator that has no more items.
# SCENARIO: Manually stepping through a list and going past the last item.
demonstrate_error("StopIteration", lambda: next(iter([1]))) # Calling next twice would trigger it
# To trigger it clearly:
def trigger_stop_iteration():
    i = iter([1])
    next(i)
    next(i)
demonstrate_error("StopIteration", trigger_stop_iteration)

# 13. AssertionError
# WHEN: An 'assert' statement fails (the condition is False).
# SCENARIO: Checking if a password is long enough, and it isn't.
def trigger_assertion():
    assert 1 == 2, "One does not equal two!"
demonstrate_error("AssertionError", trigger_assertion)

# 14. NotImplementedError
# WHEN: An abstract method that is supposed to be overridden in a subclass is called.
# SCENARIO: A base class defines 'save()' but doesn't implement it yet.
def trigger_not_implemented():
    raise NotImplementedError("This feature is coming soon!")
demonstrate_error("NotImplementedError", trigger_not_implemented)

print("--- End of Runtime Errors Demo ---")
