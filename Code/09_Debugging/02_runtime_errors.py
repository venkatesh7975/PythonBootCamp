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

print("--- End of Runtime Errors Demo ---")
