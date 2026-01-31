"""
02_runtime_errors.py - Understanding Runtime Errors (Exceptions)

Runtime errors occur while the program is running, even if the syntax is correct.
These are also known as Exceptions.
"""

print("--- Runtime Errors Demo ---\n")

def demonstrate_error(error_name, code_block):
    print(f"Testing for: {error_name}")
    try:
        code_block()
    except Exception as e:
        print(f"CAUGHT ERROR: {type(e).__name__} - {e}\n")

# 1. ZeroDivisionError
demonstrate_error("ZeroDivisionError", lambda: 10 / 0)

# 2. TypeError
demonstrate_error("TypeError", lambda: "10" + 5)

# 3. ValueError
demonstrate_error("ValueError", lambda: int("hello"))

# 4. NameError
demonstrate_error("NameError", lambda: undefined_variable + 1)

# 5. IndexError
demonstrate_error("IndexError", lambda: [1, 2, 3][10])

# 6. KeyError
demonstrate_error("KeyError", lambda: {"name": "Alice"}["age"])

# 7. AttributeError
demonstrate_error("AttributeError", lambda: (10).append(5))

print("--- End of Runtime Errors Demo ---")
