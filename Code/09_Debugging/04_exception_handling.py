"""
04_exception_handling.py - Master Exception Handling

Exception handling is the art of predicting what might go wrong and 
providing a "Plan B" so your program doesn't crash.

Core keywords:
- try: "Try running this code."
- except: "If an error happens, do this."
- else: "If NO error happened, do this."
- finally: "No matter what happened, do this at the end."
"""

def divide_numbers(a, b):
    print(f"Attempting: {a} / {b}")
    try:
        # POTENTIAL ERROR: Division by zero or incompatible types
        result = a / b
    except ZeroDivisionError:
        # WHAT: Specific handling for division by zero.
        # SCENARIO: A user inputs 0 in a calculator.
        print("Error: You cannot divide by zero!")
    except TypeError as e:
        # WHAT: Specific handling for mixing types (e.g., 10 / "2").
        # SCENARIO: A web form sends a string when a number was expected.
        print(f"Error: Invalid input types! ({e})")
    except Exception as e:
        # WHAT: A catch-all for any other unexpected errors.
        # TIP: Use specific exceptions first, then this as a backup.
        print(f"An unexpected error occurred: {e}")
    else:
        # WHEN: This block runs ONLY if the 'try' block was discovery-free.
        # SCENARIO: Logging a successful transaction.
        print(f"Success! The result is: {result}")
    finally:
        # WHEN: This block runs ALWAYS, even if there was a crash or a 'return'.
        # SCENARIO: Closing a database connection or a file.
        print("Cleanup: Operation attempt finished.\n")

# Testing the function
divide_numbers(10, 2)   # Success case
divide_numbers(10, 0)   # ZeroDivisionError
divide_numbers(10, "2") # TypeError

# Raising a custom exception
# WHAT: Sometimes you want to trigger your own error for business logic.
# SCENARIO: A user tries to sign up but states they are -5 years old.
print("--- Custom Exception ---")
def check_age(age):
    if age < 0:
        # 'raise' manually triggers an exception
        raise ValueError("Age cannot be negative!")
    print(f"Age {age} is valid.")

try:
    check_age(-5)
except ValueError as e:
    print(f"Caught custom error: {e}")

print("\n--- Exception Handling Demo Complete ---")
